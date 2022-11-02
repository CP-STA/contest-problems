#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll rem(ll n, ll k) {
    if (n >= 0) {
        return n % k;
    }
    else {
        ll ans = k - (-n) % k;
        if (ans % k == 0) {
            return 0;
        }
        else {
            return ans;
        }
    }
}

void solve() {
    ll n, k; cin >> n >> k;
    k = rem(k, 26);
    string s; cin >> s;

    string c = "";
    for (ll i = 0; i < n; i++) {
        c += char(97 + ((ll)(s.at(i)) - 97 + k) % 26);
    }
    cout << c << endl;
}

int main() {
    solve();
}