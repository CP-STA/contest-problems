#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    vector<ll> L = {};
    vector<ll> R = {};
    for (ll i = 0; i < 4; i++) {
        ll l, r; cin >> l >> r;
        L.push_back(l);
        R.push_back(r);
    }
    ll M = max_element(L.begin(), L.end());
    ll m = min_element(R.begin(), R.end());
    cout << max(m - M, 0) << endl;
}


int main() {
    solve();
}