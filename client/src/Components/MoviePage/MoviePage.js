import React, { useState }  from 'react';
import './MoviePage.css';
import { Segment,Image, Table, Comment, Form, Button, Rating } from 'semantic-ui-react';
import poster from '../../image/image.png';

export default function MoviePage() {
  const [rating, setRating] = useState(0);
  const [maxRating, setMaxRating] = useState(5);
  const handleRate = (e, { rating, maxRating }) => {
      setRating(rating);
      setMaxRating(maxRating);
  };
  return(
    <div className="movie-container">
      <Segment className="movie-card">
         <h1>Название фильма</h1>
        <div className="movie-card-info">
          <Image className="movie-card-info-poster" src={poster}/>
          <Table definition>
            <Table.Body>

              <Table.Row>
                <Table.Cell>reset rating</Table.Cell>
                <Table.Cell>None</Table.Cell>
                <Table.Cell>Resets rating to default value</Table.Cell>
              </Table.Row>

              <Table.Row>
                <Table.Cell>set rating</Table.Cell>
                <Table.Cell>rating (integer)</Table.Cell>
                <Table.Cell>Sets the current star rating to specified value</Table.Cell>
              </Table.Row>

              <Table.Row>
                <Table.Cell>set rating</Table.Cell>
                <Table.Cell>rating (integer)</Table.Cell>
                <Table.Cell>Sets the current star rating to specified value</Table.Cell>
              </Table.Row>

              <Table.Row>
                <Table.Cell>set rating</Table.Cell>
                <Table.Cell>rating (integer)</Table.Cell>
                <Table.Cell>Sets the current star rating to specified value</Table.Cell>
              </Table.Row>

            </Table.Body>
          </Table>
        </div>
        <Segment className="movie-card-video">
          <video>

          </video>
          <Rating maxRating={maxRating} onRate={handleRate} icon='star' size='huge' />
        </Segment>
        <Comment.Group>
          <Comment>
            <Comment.Avatar as='a' src='/images/avatar/small/joe.jpg' />
            <Comment.Content>
              <Comment.Author>Joe Henderson</Comment.Author>
              <Comment.Metadata>
                <div>1 day ago</div>
              </Comment.Metadata>
              <Comment.Text>
                <p>
                  The hours, minutes and seconds stand as visible reminders that your
                  effort put them all there.
                </p>
                <p>
                  Preserve until your next run, when the watch lets you see how
                  Impermanent your efforts are.
                </p>
              </Comment.Text>
            </Comment.Content>
          </Comment>

          <Comment>
            <Comment.Avatar as='a' src='/images/avatar/small/christian.jpg' />
            <Comment.Content>
              <Comment.Author>Christian Rocha</Comment.Author>
              <Comment.Metadata>
                <div>2 days ago</div>
              </Comment.Metadata>
              <Comment.Text>I re-tweeted this.</Comment.Text>
            </Comment.Content>
          </Comment>

          <Form reply>
            <Form.TextArea />
            <Button content='Add Comment' labelPosition='left' icon='edit' primary />
          </Form>
        </Comment.Group>
      </Segment>
    </div>
  )
}
