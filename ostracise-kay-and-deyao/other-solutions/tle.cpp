
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string s;

std::string ReplaceAll(std::string str, const std::string& from, const std::string& to) {
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // Handles case where 'to' is a substring of 'from'
    }
    return str;
}

int main() {
    cin >> s;
    while (s.find("kay") != string::npos || s.find("deyao") != string::npos) {
        s = ReplaceAll(s, "kay", ""); 
        s = ReplaceAll(s, "deyao", ""); 
    }
    cout << s << endl;
}