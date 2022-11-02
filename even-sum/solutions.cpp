#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    ll n; cin >> n;
    ll ans = 0;
    for (ll i = 2; i <= n; i += 2) {
        ans += i;
    }

    cout << ans << endl;
}

int main() {
    solve();
}