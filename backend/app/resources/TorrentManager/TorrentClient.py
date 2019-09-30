from urllib.parse import urlencode
import aiohttp
import asyncio
import requests
from bencode import decode
from .TorrentTracker import TorrentTracker
import struct
from concurrent.futures import CancelledError
import bitstring


class TorrentClient:

    def __init__(self, path):
        self.tracker = TorrentTracker(path)
        self.info_hash = self.tracker.torrent.info_hash
        self.peer_id = self.tracker.torrent.peer_id
        self.reader = None
        self.writer = None
        self.CHUNK_SIZE = 10*1024
        self.buff = ''
    #     10240

    async def connect_to_peers(self):
        host = self.tracker.peers[0][0]
        port = self.tracker.peers[0][1]
        self.reader, self.writer = await asyncio.open_connection(host, port)
        print("started connection:", host + ':' + str(port))
        await self.handshake()
        # await self._send_interested()
        data = await self._stream()
        # data = b'\x00\x00\x00\xa9\x05\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0'
        # self._parse_stream(data)
        # print(data)

    async def _stream(self):
            try:
                data = await self.reader.read(self.CHUNK_SIZE)
                if data:
                    # self.buff += data
                    messsage = self._parse_stream(data)
                    return messsage
                else:
                    print('No data read from stream')
                    # if self.buffer:
                    #     message = self.parse()
                    #     if message:
                    #         return message
                    raise StopAsyncIteration()
            except ConnectionResetError:
                print('Connection closed by peer')
                raise StopAsyncIteration()
            except CancelledError:
                raise StopAsyncIteration()
            except StopAsyncIteration as e:
                raise e
            except Exception as e:
                print('Error when iterating over stream!', e)
                raise StopAsyncIteration()

    def _parse_stream(self, data):

        # def _consume():
        #     self.buff = data[header_length + message_length:]
        #
        # def _data():
        #     """"Extract the current message from the read buffer"""
        #     return data[:header_length + message_length]
        header_length = 4
        message_length = struct.unpack('>I', data[0:4])[0]
        message_id = struct.unpack('>b', data[4:5])[0]
        if message_id is PeerMessage.BitField:
            # data = _data()
            # _consume()
            parts = struct.unpack('>Ib' + str(message_length - 1) + 's', data)
            print(parts)
            return parts[2]
        else:
            print("another mes_id", message_id, data)

        # bit_str = bitstring.BitArray(bytes=data)

        #
        # print(parts)
        # print("unpacked:", message_length)
        # for d in data:
        #     print(d)

    async def handshake(self):
        handshake_len = 68
        encoded_struct = self._encode_struct()
        self.writer.write(encoded_struct)
        await self.writer.drain()
        buf = b''
        while len(buf) < handshake_len:
            buf = await self.reader.read(self.CHUNK_SIZE)
        # print(buf)
        parts = struct.unpack('>B19s8x20s20s', buf[:handshake_len])
        mes = await self.reader.read(self.CHUNK_SIZE)
        # print(parts)
        # print(buf[handshake_len:])
        # print("info:", parts[2], "peer_id:", parts[3])
        # return buf[handshake_len:]

    def _encode_struct(self):
        info_hash = self.info_hash
        peer_id = self.peer_id
        if isinstance(self.info_hash, str):
            info_hash = self.info_hash.encode('utf-8')
        if isinstance(self.peer_id, str):
            peer_id = self.peer_id.encode('utf-8')
        encoded_struct = struct.pack(
            '>B19s8x20s20s',
            19,
            b'BitTorrent protocol',

            info_hash,
            peer_id
        )
        return encoded_struct

    async def _send_interested(self):
        message = struct.pack('>Ib', 1, PeerMessage.Interested)
        self.writer.write(message)
        await self.writer.drain()



class PeerMessage:
    Choke = 0
    Unchoke = 1
    Interested = 2
    NotInterested = 3
    Have = 4
    BitField = 5
    Request = 6
    Piece = 7
    Cancel = 8
    Port = 9
