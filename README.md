# Hypertube
A streaming service for watching videos through the BitTorrent protocol

Full specification: https://cdn.intra.42.fr/pdf/pdf/1209/hypertube.en.pdf

[Server] Python (Flask)

[Client] React

[Database] PostgreSQL

[Deployment] Docker

Goals:

- Everything must be secured (JWT, SQL-debugging, XSS)
- Omniauth
- The search engine of videos
- Stream the video flux
- Convertion of video format to mkv, mp4
- Leaving a comment on the video
- The details of a video (summary, casting, length and so on)

P.S  When two people “like” each other, we will say that they are “connected” and are now able to chat
## Getting Started

#### Install npm
brew install node

#### Install docker

You can use two variants.
The first one:
```
https://docs.docker.com/compose/install/
```
The second one:
```
brew install docker docker-machine docker-compose
docker-machine create --driver virtualbox Matcha
eval $(docker-machine env Matcha)
```

## Build and Run

```
git clone https://github.com/AndreiSukharev/hypertube.git hypertube
cd matcha
docker-compose up --build
cd client
npm i
npm run serve
go to: http://localhost:8080
```

#### Test

Create test entities:
```
docker exec flask_hyper bash -c "python test_entities.py"
```
#### Note Docker

Run postgres client:

```
docker exec -it postgres_hyper psql schoolDB user
```
Enter in container:
```
docker exec -it flask_hyper bash
```
Remove all:
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```
