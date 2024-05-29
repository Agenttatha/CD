using namespace std;

void calculateFirstSets(unordered_map<char,unordered_set<char>> &first,unordered_map<char,vector<string>> &grammar){

    for(auto it:grammar){
        char nonTerminal=it.first;
        for(auto production:it.second){
            char firstSymbol=production[0];
            if(islower(firstSymbol)||firstSymbol=='#'){
                first[nonTerminal].insert(firstSymbol);
            } else{
                for(char terminal:first[firstSymbol]){
                    first[nonTerminal].insert(terminal);
                }
            }
        }
    }
}

// Function to calculate Follow sets
void calculateFollowSets(unordered_map<char, unordered_set<char>>& follow, unordered_map<char, vector<string>>& grammar, char startSymbol) {
    follow[startSymbol].insert('$'); // $ is added to Follow of start symbol
    for (auto& rule : grammar) {
        char nonTerminal = rule.first;
        for (auto& production : rule.second) {
            for (int i = 0; i < production.size(); i++) {
                if (isupper(production[i])) {
                    if (i == production.size() - 1 || production[i + 1] == '#') {
                        // If non-terminal is the last symbol or epsilon follows it, add Follow of LHS
                        for (char terminal : follow[nonTerminal]) {
                            follow[production[i]].insert(terminal);
                        }
                    } else {
                        // Add First of next symbol after non-terminal
                        char nextSymbol = production[i + 1];
                        if (islower(nextSymbol) || nextSymbol == '#') {
                            follow[production[i]].insert(nextSymbol);
                        } else {
                            for (char terminal : follow[nextSymbol]) {
                                follow[production[i]].insert(terminal);
                            }
                        }
                    }
                }
            }
        }
    }
}

int main() {
    unordered_map<char, vector<string>> grammar = {
        {'S', {"AB", "bBA"}},
        {'A', {"a", "#"}},
        {'B', {"b", "#"}}
    };

    unordered_map<char, unordered_set<char>> first, follow;

    calculateFirstSets(first, grammar);
    calculateFollowSets(follow, grammar, 'S');

    cout << "First sets:\n";
    for (auto& entry : first) {
        cout << entry.first << ": { ";
        for (char terminal : entry.second) {
            cout << terminal << " ";
        }
        cout << "}\n";
    }

    cout << "\nFollow sets:\n";
    for (auto& entry : follow) {
        cout << entry.first << ": { ";
        for (char terminal : entry.second) {
            cout << terminal << " ";
        }
        cout << "}\n";
    }

    return 0;
}
