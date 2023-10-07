#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    ll N; cin >> N;
    string S = " ";
    for (ll i = 0; i < N; i++) {
        string s; cin >> s;
        S += s.at(0);
    }
    string T; cin >> T;
    T = " " + T;

    ll Ls = S.size();
    ll Lt = T.size();

    vector<vector<ll>> dp = {};
    for (ll i = 0; i < Ls; i++) {
        vector<ll> cand = {};
        for (ll j = 0; j < Lt; j++) {
            cand.push_back(0);
        }
        dp.push_back(cand);
    }
    for (ll i = 1; i < Ls; i++) {
        for (ll j = 1; j < Lt; j++) {
            if (S.at(i) == T.at(j)) {
                dp.at(i).at(j) = max({dp.at(i - 1).at(j), dp.at(i).at(j - 1), dp.at(i - 1).at(j - 1) + 1});
            }
            else {
                dp.at(i).at(j) = max({dp.at(i - 1).at(j), dp.at(i).at(j - 1)});
            }
        }
    }
    
    if (Lt - 1 == dp.at(Ls - 1).at(Lt - 1)) {
        cout << "Yes" << endl;
    }
    else {
        cout << "No" << endl;
    }
}

int main() {
    solve();
}