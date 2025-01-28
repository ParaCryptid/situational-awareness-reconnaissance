from hashlib import sha256
import time

class Blockchain:
    def __init__(self):
        """
        Initialize a simple blockchain for secure collaboration.
        """
        self.chain = []
        self.create_block(previous_hash="0")  # Genesis block

    def create_block(self, data=None, previous_hash=None):
        """
        Create a new block and add it to the chain.
        :param data: Data to store in the block (default: None).
        :param previous_hash: Hash of the previous block (default: None).
        :return: The new block.
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "data": data,
            "previous_hash": previous_hash or self.hash(self.chain[-1]) if self.chain else "0"
        }
        block["hash"] = self.hash(block)
        self.chain.append(block)
        return block

    def hash(self, block):
        """
        Generate a SHA-256 hash of the block.
        :param block: The block to hash.
        :return: The hash of the block.
        """
        block_string = f"{block['index']}{block['timestamp']}{block['data']}{block['previous_hash']}"
        return sha256(block_string.encode()).hexdigest()

    def is_valid_chain(self):
        """
        Validate the blockchain integrity.
        :return: True if the chain is valid, otherwise False.
        """
        for i in range(1, len(self.chain)):
            if self.chain[i]["previous_hash"] != self.hash(self.chain[i - 1]):
                return False
        return True

# Example usage
# blockchain = Blockchain()
# blockchain.create_block(data={"message": "Intelligence update"})
# blockchain.create_block(data={"message": "New analysis completed"})
# print(blockchain.chain)
# print("Blockchain valid:", blockchain.is_valid_chain())
