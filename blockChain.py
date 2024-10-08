import datetime
import hashlib
import json

class Block:
    def __init__(self, previous_hash, data):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = str(datetime.datetime.now().isoformat())
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
      
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("0", "Genesis Block")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def append(self, data):
        last_block = self.get_last_block()
        previous_hash = last_block.hash
        new_block = Block(previous_hash, data)
        self.chain.append(new_block)

    def print_blockchain(self):
        for idx, block in enumerate(self.chain):
            print(f"Block {idx}:")
            print(f"Data: {block.data}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print('-------------------------')

    def verify_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.compute_hash():
                return False

        return True

    def verify_and_print(self):
        is_valid = self.verify_blockchain()
        self.print_blockchain()
        print(f"Blockchain valid: {is_valid}")
        return is_valid

    def change_block_data(self, index, new_data):
        if 0 <= index < len(self.chain):
            self.chain[index].data = new_data
           
            self.chain[index].hash = self.chain[index].compute_hash()
        else:
            print("Invalid block index!")

    def number_of_blocks(self):
        return len(self.chain)


def menu():
    blockchain = Blockchain()

    while True:
        print("\nBlockchain Menu:")
        print("1. Add a new block.")
        print("2. Show the last block.")
        print("3. Show the whole blockchain.")
        print("4. Verify the blockchain.")
        print("5. Verify and print the blockchain.")
        print("6. Change data of a particular block.")
        print("7. Show number of blocks.")
        print("8. End the script.")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            data = input("Enter block data: ")
            blockchain.append(data)
            print("Block added.")

        elif choice == '2':
            last_block = blockchain.get_last_block()
            print(f"Data: {last_block.data}")
            print(f"Timestamp: {last_block.timestamp}")
            print(f"Previous Hash: {last_block.previous_hash}")
            print(f"Hash: {last_block.hash}")

        elif choice == '3':
            blockchain.print_blockchain()

        elif choice == '4':
            is_valid = blockchain.verify_blockchain()
            print(f"Blockchain valid: {is_valid}")

        elif choice == '5':
            blockchain.verify_and_print()

        elif choice == '6':
            index = int(input("Enter the block index to modify: "))
            new_data = input("Enter the new block data: ")
            blockchain.change_block_data(index, new_data)
            print("Block data updated.")

        elif choice == '7':
            print(f"Number of blocks: {blockchain.number_of_blocks()}")

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    menu()
