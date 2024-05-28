from collections import defaultdict
def findClosure(closure):
    while 1:
        n = len(closure)
        temp_cl = closure.copy()
        for lhs, rhs in closure:
            if rhs[-1] == '.':
                continue
            dot_index = rhs.index('.')
            B = rhs[dot_index+1]
            if B.isupper():
                for prod in CFG[B]:
                    item = (B, '.'+prod)
                    if item not in temp_cl:
                        temp_cl.append(item)
        closure = temp_cl
        if len(closure) == n:
            return closure

def findGOTO(state_num):
    global count
    closure = states[state_num]
    new = set()
    gotos = defaultdict(list)
    for lhs, rhs in closure:
        if rhs[-1] == '.':
            continue
        dot_index = rhs.index('.')
        charNextToDot = rhs[dot_index+1]
        rhs = rhs[:dot_index] + charNextToDot + '.' + rhs[dot_index+2:]
        new_cl = [(lhs, rhs)]
        new_cl = findClosure(new_cl)
        gotos[charNextToDot].extend(new_cl)

    for lhs, new_cl in gotos.items():
        for num, cl in states.items():
            if new_cl == cl:
                statemap[(state_num, lhs)] = num
                break
        else:
            count += 1
            states[count] = new_cl
            statemap[(state_num, lhs)] = count
            new.add(count)
    return new

def GOTO(num):
    new = findGOTO(num)
    while 1:
        n = len(new)
        new1 = new.copy()
        for i in new:
            new1 |= findGOTO(i)
        new = new1
        if len(new) == n:
            break

def compute_first(variable):
    first = set()
    productions = [rule[1] for rule in rules if rule[0] == variable]
    for production in productions:
        if production[0] == variable:
            continue
        if not production[0].isupper():
            first.add(production[0])
        else:
            for x in production:
                first |= compute_first(x)
                if "ε" not in first:
                    break
    return first

def compute_follow(variable):
    follow = set()
    if variable == start_symbol:
        follow.add("$")
    for rule in rules:
        for j, char in enumerate(rule[1]):
            if char == variable:
                while j < len(rule[1]) - 1:
                    if not rule[1][j + 1].isupper():
                        follow.add(rule[1][j + 1])
                        break
                    else:
                        follow |= compute_first(rule[1][j + 1])
                        if "ε" not in compute_first(rule[1][j + 1]):
                            break
                    j += 1
                else:
                    if rule[0] != variable:
                        follow |= compute_follow(rule[0])
    follow.discard("ε")
    return follow

def SLR():
    cols = T + ['$'] + NT
    Table = [['']*len(cols) for _ in range(count+1)]
    for map, s in statemap.items():
        num, char = map
        index = cols.index(char)
        if char in NT:
            Table[num][index] = f'{s}'
        else:
            Table[num][index] = f'S{s}'
    for num, cl in states.items():
        for lhs, rhs in cl:
            if rhs[-1] == '.':
                if rhs[0] == start_symbol and lhs == new_start_symbol:
                    index = cols.index('$')
                    Table[num][index] = 'Accept'
                else:
                    prod_num = rules.index((lhs, rhs[:-1]))
                    follow = compute_follow(lhs)
                    for i in follow:
                        index = cols.index(i)
                        Table[num][index] = f'R{prod_num+1}'
    print("\nSLR(1) parsing table:\n")
    frmt = "{:>8}" * len(cols)
    print("   ", frmt.format(*cols), "\n")
    ptr = 0
    j = 0
    for y in Table:
        print(f"{{:>3}} {frmt.format(*y)}".format('I' + str(j)))
        j += 1

# Test Case - 1
CFG = {'E': ['E+T', 'T'],
       'T': ['T*F', 'F'],
       'F': ['(E)', 'i']}

T = ['+', '*', '(', ')', 'i']

# test case -2
# CFG = {'S': ['E'],
#        'E': ['E+T', 'T'],
#        'T': ['T*F', 'F'],
#        'F': ['i']}
#
# T = ['+', '*', 'i']

# test case - 3
# CFG = {'S': ['CC'],
#        'C': ['cC', 'd']}
#
# T = ['c', 'd']

new_start_symbol = 'Z'
NT = list(CFG.keys())
rules = [(head, body) for head, bodies in CFG.items() for body in bodies]
start_symbol = rules[0][0]
closure = [(new_start_symbol, '.' + start_symbol)]
I0 = findClosure(closure)
states = {0: I0}
statemap = {}
count = 0
GOTO(0)
SLR()
