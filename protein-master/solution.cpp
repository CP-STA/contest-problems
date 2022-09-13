#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    ll q; cin >> q;
    map<ll, string> dic = {};
    set<ll> protein = {};
    while (q > 0) {
        string s; cin >> s;
        if (s == "IN") {
            q--;
            string vege_name; ll quantity; cin >> vege_name >> quantity;
            dic[quantity] = vege_name;
            protein.insert(quantity);
        }
        else if (s == "OUT") {
            auto itr = protein.begin();
            itr++;
            cout << dic[*itr] << endl;
            q--;
        }
    }
}

int main() {
    solve();
}