import re


class Lexer():
    def __init__(self, source):
        self.source = source
    
    def tokinize(self):
        tokens = []
        source = self.source.split()
        idx = 0
        while idx < len(source):
            word = source[idx]
            if word == 'lok':
                tokens.append(['LOK_DECLERATION', word])
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word.endswith(';'):
                    tokens.append(['IDENTIFIER', word[:len(word)-1]])
                else:
                    tokens.append(['IDENTIFIER', word])
            elif re.match('[0-9]', word):
                if word.endswith(';'):
                    tokens.append(['INTEGER', word[:len(word)-1]])
                else:
                    tokens.append(['INTEGER', word])
            elif word in '=/*=-+':
                tokens.append(['OPERATOR', word])

            if word.endswith(';'):
                tokens.append(['STATEMENT_END', ';'])


            idx += 1
        
        return tokens
