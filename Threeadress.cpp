

int precedence(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

void func(string &expression){
    stack<string> operands;
    stack<char> operators;
    vector<string> threeaddr;

    for(char ch:expression){
        if(isspace(ch)) continue;

        else if(isalpha(ch)||isdigit(ch)){
            string operand(1, ch);
            operands.push(operand);
        }
        else if(ch=='(') operators.push(ch);

        else if(ch==')'){
            while(!operators.empty() and operators.top()!='('){
                string op1=operands.top();
                operands.pop();
                string op2=operands.top();
                operands.pop();
                char op=operators.top();
                operators.pop();
                int len=threeaddr.size()+1;
                string temp = "t" + to_string(threeaddr.size() + 1);
                threeaddr.push_back(temp + " = " + op1 + " " + op + " " + op2);
                operands.push(temp);
            }
            operators.pop();
        }
        else{
            while(!operators.empty() and precedence(operators.top())>=precedence(ch)){
                string op1=operands.top();
                operands.pop();
                string op2=operands.top();
                operands.pop();
                char op=operators.top();
                operators.pop();
                int len=threeaddr.size()+1;
                string temp = "t" + to_string(threeaddr.size() + 1);
                threeaddr.push_back(temp + " = " + op1 + " " + op + " " + op2);
                operands.push(temp);
            }
            operators.push(ch);
        }
    }
      while (!operators.empty()) {
        string op2 = operands.top();
        operands.pop();
        string op1 = operands.top();
        operands.pop();
        char op = operators.top();
        operators.pop();
        string temp = "t" + to_string(threeaddr.size() + 1);
        threeaddr.push_back(temp + " = " + op1 + " " + op + " " + op2);
        operands.push(temp);
    }
    for(auto it:threeaddr){
        cout<<it<<endl;
    }
}

int main() {
    string expr="a=(b+c)*((d-e)/f)";
    func(expr);
}
