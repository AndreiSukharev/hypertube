from hashlib import sha1
from bencode import encode, decode
import random


class TorrentParser:

    def __init__(self, path):
        self.torrent = self.decode_from_bencode(path)
        self.announce = self.torrent['announce']
        self.info = self.torrent['info']
        self.peer_id = self.generate_peer_id()
        self.info_hash = self.get_info_hash(self.torrent)
        self.left = self.get_length()

    def get_length(self):
        return 1485881344
        # return self.info['length']

    @staticmethod
    def generate_peer_id():
        return '-PC0001-' + ''.join(
            [str(random.randint(0, 9)) for _ in range(12)])

    @staticmethod
    def get_info_hash(torrent):

        info = encode(torrent['info'])
        encoded_hash = sha1(info).digest()
        # print("orig", torrent['info'])
        # print("encoded", info)
        return encoded_hash

    @staticmethod
    def decode_from_bencode(path):
        with open(path, 'rb') as f:
            meta_info = f.read()
            # torrent = Decoder(meta_info).decode()
            torrent = decode(meta_info)
            print(torrent)
            return torrent
