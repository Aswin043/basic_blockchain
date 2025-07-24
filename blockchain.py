class blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self, block):
        pass

    def new_transaction(self):
        return self.chain
    @staticmethod
    def hash(block):
        pass
    @property
    def last_block(self):
        pass

    def __repr__(self):
        return f"Blockchain with {len(self.chain)} blocks"