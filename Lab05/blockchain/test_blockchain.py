import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block with index 0
        genesis_block = Block(0, "0", time.time(), [], 100)
        self.chain.append(genesis_block)

    def get_previous_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.transactions.append({"sender": sender, "recipient": recipient, "amount": amount})

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain), previous_hash, time.time(), self.transactions, proof)
        self.transactions = []  # Reset the list of transactions after the block is created
        self.chain.append(block)
        return block

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            current_block = chain[block_index]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            previous_block = current_block
            block_index += 1
        return True

# Test the blockchain
my_blockchain = Blockchain()

# Add some transactions
my_blockchain.add_transaction('Alice', 'Bob', 1)
my_blockchain.add_transaction('Bob', 'Charlie', 2)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

# Mine a block
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Alice', 1)
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Display the blockchain
for block in my_blockchain.chain:
    print(f"Block {block.index}")
    print("Timestamp: ", block.timestamp)
    print("Transactions: ", block.transactions)
    print("Proof: ", block.proof)
    print("Previous Hash: ", block.previous_hash)
    print("Hash: ", block.hash)
    print("---------------------------------")

# Check if the blockchain is valid
print("Is the blockchain valid? ", my_blockchain.is_chain_valid(my_blockchain.chain))
