#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    string S; cin >> S;
    bool flail = false;
    for (ll i = 0; i + 2 < 12; i++) {
        if (S.at(i) == 'x' && S.at(i + 1) == 'x' && S.at(i + 2) == 'x') {
            flail = true;
        }
    }
    if (flail) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}

int main() {
    solve();
}