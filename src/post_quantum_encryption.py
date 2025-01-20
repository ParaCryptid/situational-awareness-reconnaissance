from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
import os

class PostQuantumEncryptor:
    def __init__(self):
        """
        Initialize the encryption system with key pairs.
        """
        self.private_key = x25519.X25519PrivateKey.generate()
        self.public_key = self.private_key.public_key()

    def generate_shared_key(self, peer_public_key):
        """
        Generate a shared key using the peer's public key.
        :param peer_public_key: The public key of the peer.
        :return: A shared secret key.
        """
        shared_key = self.private_key.exchange(peer_public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'post-quantum encryption',
        ).derive(shared_key)
        return derived_key

# Example usage
# alice = PostQuantumEncryptor()
# bob = PostQuantumEncryptor()
# shared_key = alice.generate_shared_key(bob.public_key)
# print("Shared Key:", shared_key)
