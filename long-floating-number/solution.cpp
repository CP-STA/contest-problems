#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    string S; cin >> S;
    if (S.at(0) == '0') {
        cout << "smaller" << endl;
    }
    else {
        ll cnt = 0;
        for (ll i = 2; i < S.size(); i++) {
            if (S.at(i) != '0') {
                cnt++;
            }
        }
        if (cnt > 0) {
            cout << "larger" << endl;
        }
        else {
            cout << "equal" << endl;
        }
    }
}


int main() {
    solve();
}