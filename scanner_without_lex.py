import re


# Define token types
TOKEN_TYPES = {
    'KEYWORD': r'(int|float|char|if|else|for|while|return)',
    'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9]*',
    'INTEGER_CONSTANT': r'\d+',
    'FLOAT_CONSTANT': r'\d+\.\d+',
    'OPERATOR': r'[\+\-\*/=<>]',
    'PUNCTUATION': r'[();{},]',
    'WHITESPACE': r'\s+'
}


# Tokenize function
# Tokenize function
def tokenize(code):
    tokens = []
    for line in code.split('\n'):
        p = 0
        while p < len(line):
            match = None
            for token_type, pattern in TOKEN_TYPES.items():
                regex = re.compile(pattern)
                token = regex.match(line, p)
                if token:
                    value = token.group(0)
                    if token_type != 'WHITESPACE':
                        tokens.append((token_type, value))
                    p = token.end()
                    break
            if not token:
                # If no match is found, increment p by 1 to avoid infinite loop
                p += 1
    return tokens




# Example code
code = """
int main() {
    int a = 10;
    float b = 3.14;
    if (a < b) {
        printf("a is less than b");
    } else {
        printf("a is greater than or equal to b");
    }
    return 0;
}
"""


# Tokenize the code
tokens = tokenize(code)


# Print tokens
for token in tokens:
    print(token)
