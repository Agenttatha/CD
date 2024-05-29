#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

struct Three {
    string temp;
    vector<string> data;
};

vector<Three> process_input_data(const vector<string>& input_data) {
    vector<Three> s;
    for (const string& line : input_data) {
        istringstream iss(line);
        vector<string> parts;
        string part;
        while (iss >> part) {
            parts.push_back(part);
        }
        if (parts.size() > 1) {
            s.push_back({parts[0], vector<string>(parts.begin() + 1, parts.end())});
        }
    }

    for (const Three& item : s) {
        if (item.data.size() > 1 && item.data[0] == "=") {
            cout << "LDA " << item.data[1] << endl;
            if (item.data.size() > 3 && item.data[2] == "+") {
                cout << "ADD " << item.data[3] << endl;
            }
            if (item.data.size() > 3 && item.data[2] == "-") {
                cout << "SUB " << item.data[3] << endl;
            }
            cout << "STA " << item.temp << endl;
        }
    }
    return s;
}

int main() {
    cout << "Test Case 1" << endl;
    vector<string> input_data_1 = {"t1 = a + b", "t2 = t1 + c", "out = t2"};
    process_input_data(input_data_1);

    cout << "\nTest Case 2" << endl;
    vector<string> input_data_2 = {"x = a + b", "y = x - c", "z = y + d"};
    process_input_data(input_data_2);

    cout << "\nTest Case 3" << endl;
    vector<string> input_data_3 = {"t1 = in1 - in2", "out = t1"};
    process_input_data(input_data_3);

    return 0;
}
