class Three:
    def __init__(self, temp, data):
        self.data = data
        self.temp = temp
def process_input_data(input_data):
    s = []
    for line in input_data:
        parts = line.split()
        s.append(Three(parts[0], parts[1:]))
    for i in range(len(s)):
        if s[i].data[0] == "=":
            print("LDA " + s[i].data[1])
            if len(s[i].data) > 2 and s[i].data[2] == "+":
                print("ADD " + s[i].data[3])
            if len(s[i].data) > 2 and s[i].data[2] == "-":
                print("SUB " + s[i].data[3])
            print("STA " + s[i].temp)

print("Test Case 1")
input_data_1 = ["t1 = a + b", "t2 = t1 + c", "out = t2"]
process_input_data(input_data_1)
print("\nTest Case 2")
input_data_2 = ["x = a + b", "y = x - c", "z = y + d"]
process_input_data(input_data_2)
print("\nTest Case 3")
input_data_3 = ["t1 = in1 - in2", "out = t1"]
process_input_data(input_data_3)