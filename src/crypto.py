import nacl.uitls
from nacl.public import PrivateKey, Box

class Crypto:
    def __init__(self, key_dir):
        self.key_dir = key_dir

    def create_keys(self):
        sk = PrivateKey.generate()
        pk = sk.public_key

        return sk, pk
    def exchange(self, self_sk, reciever_pk):
        return Box(self_sk, reciever_pk)
        
