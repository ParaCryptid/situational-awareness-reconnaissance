
from src.post_quantum_encryption import PostQuantumEncryptor

def test_post_quantum_encryption():
    alice = PostQuantumEncryptor()
    bob = PostQuantumEncryptor()
    assert alice.generate_shared_key(bob.public_key) is not None
