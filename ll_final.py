class First_Follow():
    def __init__(self, grammar):
        self.grammar = grammar
        self.non_terminals = grammar.keys()
        print(self.non_terminals)
        self.start = list(self.non_terminals)[0]
        self.rules = [(head, body) for head, bodies in grammar.items() for body in bodies]
 
    def compute_first(self, variable):
        first = set()
 
        productions = [rule[1] for rule in self.rules if rule[0] == variable]
 
        for production in productions:
            if not production[0].isupper():
                first.add(production[0])
            else:
                first |= self.compute_first(production[0])

 
        return first
 
    def compute_follow(self, variable):
 
        follow = set()
 
        if variable == self.start:
            follow.add('$')
 
        for rule in self.rules:
            for j, char in enumerate(rule[1]):
                if char == variable:
                    while j < len(rule[1]) - 1:
                        if not rule[1][j + 1].isupper():
                            follow.add(rule[1][j + 1])
                            break
                        else:
                            follow |= self.compute_first(rule[1][j + 1])
                            if '@' not in self.compute_first(rule[1][j + 1]):
                                break
                        j += 1
                    else:
                        if rule[0] != variable:
                            follow |= self.compute_follow(rule[0])
        follow.discard('@')
        return follow
 
    def print_sets(self):
        print("First Sets:")
        for non_terminal in self.non_terminals:
            print(f"{non_terminal}: {self.compute_first(non_terminal)}")
 
        print("\nFollow Sets:")
        for non_terminal in self.non_terminals:
            print(f"{non_terminal}: {self.compute_follow(non_terminal)}")
 
    def computeFirstOneRHS(self, variable):
        first = set()
 
        if not variable[0].isupper():
            first.add(variable[0])
        else:
            for x in variable:
                first |= self.compute_first(x)
                if '@' not in first:
                    break
 
        return first
 
    def compute_parsing_table(self):
        print('\nParsing Table')
        table = {}
 
        for rule in self.rules:
            rule1, rule2 = rule
            first = list(self.computeFirstOneRHS(rule2))
            if '@' in first:
                first.extend(self.compute_follow(rule1))
                while '@' in first:
                    first.remove('@')
 
            for terminal in first:
                key = (rule1, terminal)
                if key in table:
                    table[key].append(rule2)
                else:
                    table[key] = [rule2]
 
        for key, value in table.items():
            print(f'{key} : {value}')
 
        return table
 
 
# @
def main():
    example_grammar = {
    'E': ['TA'],
    'A': ['+TA', '@'],
    'T': ['FB'],
    'B': ['*FB', '@'],
    'F': ['(E)', 'i']
    }
   
    ff = First_Follow(example_grammar)
 
    ff.print_sets()
    ans = ff.compute_parsing_table()
    print(ans)
 
if __name__ == '__main__':
    main()
