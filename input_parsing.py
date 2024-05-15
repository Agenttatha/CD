class SLRParser:
    def __init__(self):
        self.stack = [0]  
        self.input_string = ""
        self.current_index = 0
        self.accepted = False
        self.grammar=[['E','E+T'],['E','T'],['T','T*F'],['T','F'],['F','(E)'],['F','i']]
        self.parse_table = {
            (0, 'i'): "S5", (0, '('): "S4", (0, "E"): 1,(0,"T"):2,(0,"F"):3,
            (1, '$'): "Accept", (1,"+"):"S6",
            (2, '*'): "S7", (2, '+'): "R2", (2,")"):"R2", (2,"$"):"R2",
            (3, '*'): "R4", (3, '$'): "R4", (3,"+"):"R4", (3,")"):"R4",
            (4, 'i'): "S5", (4, '('): "S4", (4,"E"):8, (4,"T") : 2,(4,"F") : 3,
            (5, '*'): "R6", (5, '$'): "R6", (5,"+"):"R6", (5,")"):"R6",
            (6, 'i') : "S5", (6,"("):"S4", (6,"T"):9, (6, "F"):3,
            (7,'i') : "S5", (7,"("):"S4", (7,"F"):10,
            (8, ')'): "S11", (8, '+'): "S6", (8, '$'): "R6",
            (9, '*'): "S7", (9, '$'): "R1", (9, ")"):"R1", (9,"$"):"R1",
            (10,"+"):"R3", (10, "*") :"R3", (10, ")"):"R3", (10,"$") : "R3",
            (11, '$'): "R5", (11,")") : "R5",(11,"*"):"R5",(11,"+"):"R5"
        }
        self.states=11
    def parse(self, input_string):
        self.input_string = input_string + "$"
        while not self.accepted:
            state = self.stack[-1]
            symbol = self.input_string[self.current_index]
            action = self.parse_table.get((state, symbol))
            print(state,symbol,action)
            if action is None:
                print("Error: Invalid input at position", self.current_index)
                print("String is not accepted")
                return
            if action == "Accept":
                print("Accepted: Input parsed successfully!")
                self.accepted = True
                return
            if action.startswith("S"):
                self.stack.append(symbol)
                self.stack.append(int(action[1:]))
                self.current_index += 1
            elif action.startswith("R"):
                production_num = int(action[1:])
                n=int(len(self.grammar[production_num-1][1]))*2
                self.stack=self.stack[:-n]
                top=self.stack[-1]
                x=self.grammar[production_num-1][0]
                self.stack.append(x)
                act=self.parse_table.get((top,x))
                if(not(act<=self.states and act>=0)):
                    print("Rejected string")
                    return
                self.stack.append(act)
            else:
                print("Error: Invalid action", action)
                return
parser = SLRParser()
input_string = "i+i*i"
parser.parse(input_string)