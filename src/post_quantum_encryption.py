from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class PostQuantumEncryptor:
    def __init__(self):
        """Initialize the encryption system with key pairs."""
        self.private_key = x25519.X25519PrivateKey.generate()
        self.public_key = self.private_key.public_key()
        logging.info("Post-quantum key pair generated.")

    def generate_shared_key(self, peer_public_key_bytes: bytes) -> bytes:
        """
        Derive a shared key using peer's public key.
        :param peer_public_key_bytes: The peer's public key in bytes.
        :return: The derived shared key.
        """
        peer_public_key = x25519.X25519PublicKey.from_public_bytes(peer_public_key_bytes)
        shared_key = self.private_key.exchange(peer_public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'post-quantum encryption'
        ).derive(shared_key)
        logging.info("Shared key derived successfully.")
        return derived_key

    def export_public_key(self) -> bytes:
        """
        Export the public key as bytes.
        :return: Serialized public key.
        """
        return self.public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
