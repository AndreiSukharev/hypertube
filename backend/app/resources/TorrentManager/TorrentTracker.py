from .TorrentParser import TorrentParser
from urllib.parse import urlencode
import aiohttp
import requests
from bencode import decode


class TorrentTracker:

    def __init__(self, path):
        self.torrent = TorrentParser(path)
        self.interval = None
        self.peers = None
        self.connect_to_tracker()
        # self.http_client = aiohttp.ClientSession()

    def connect_to_tracker(self,
                           first: bool = None,
                           uploaded: int = 0,
                           downloaded: int = 0):
        params = {
            'info_hash': self.torrent.info_hash,
            'peer_id': self.torrent.peer_id,
            'port': 6889,
            'left': self.torrent.left - downloaded,
            'uploaded': uploaded,
            'downloaded': downloaded,
            'compact': 1,
            'event': 'started'
        }
        url = self.torrent.announce + '?' + urlencode(params)
        print("connection to tracker: " + url)
        req = requests.get(url)
        res = decode(req.content)
        self.interval = res['interval']
        self.peers = self.parse_peers(res['peers'])
        # print(res)
        # print(self.peers)
        # print(self.interval)
        # print(req.json())
        # print(req.content)
        # return url

    def parse_peers(self, peers):
        i = 1
        host = ''
        port = 0
        arr_peers = []
        for peer in peers:
            if i == 1:
                host = str(peer)
            elif i <= 4:
                host += '.' + str(peer)
            elif i == 5:
                port = peer * 256
            elif i == 6:
                port += peer
                sock = (host, port)
                arr_peers.append(sock)
                i = 0
            i += 1
        return arr_peers



