

class Parser():

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = 0

    def parse(self):
        
        while self.token_idx < len(self.tokens):
            token_type = self.tokens[self.token_idx][0]
            token_value = self.tokens[self.token_idx][1]

            print(token_type, token_value)
            self.token_idx += 1