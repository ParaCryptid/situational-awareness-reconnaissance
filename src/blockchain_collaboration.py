import time
import json
import logging
from hashlib import sha256
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Blockchain:
    def __init__(self):
        """Initialize a simple blockchain for secure collaboration."""
        self.chain = []
        self.create_block(data="Genesis Block", previous_hash="0")

    def create_block(self, data: Any, previous_hash: Optional[str] = None) -> Dict:
        """
        Create a new block and add it to the chain.
        :param data: Data to store in the block.
        :param previous_hash: Hash of the previous block.
        :return: The new block.
        """
        previous_hash = previous_hash or self.get_last_block()["hash"]
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': data,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        logging.info(f"Block created: {block}")
        return block

    def hash_block(self, block: Dict) -> str:
        """
        Create a SHA-256 hash of a block.
        :param block: The block to hash.
        :return: The hash string.
        """
        block_copy = block.copy()
        block_copy.pop('hash', None)
        encoded_block = json.dumps(block_copy, sort_keys=True).encode()
        return sha256(encoded_block).hexdigest()

    def get_last_block(self) -> Dict:
        """Return the last block in the chain."""
        return self.chain[-1]

    def is_chain_valid(self) -> bool:
        """Verify the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr["previous_hash"] != prev["hash"]:
                return False
            if curr["hash"] != self.hash_block(curr):
                return False
        return True
