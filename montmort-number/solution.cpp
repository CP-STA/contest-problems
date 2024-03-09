#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll factorial(ll N) {
    ll ans = 1;
    for (ll i = 1; i <= N; i++) {
        ans *= i;
    }
    return ans;
}

void solve() {
    ll N; cin >> N;

    ll ans = 0;
    for (ll k = 2; k <= N; k++) {
        if (k % 2 == 0) {
            ans += factorial(N) / factorial(k);
        }
        else {
            ans -= factorial(N) / factorial(k);
        }
    }
    cout << ans << endl;
}

int main() {
    solve();
}