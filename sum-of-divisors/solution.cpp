#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    ll n; cin >> n;
    ll ans = 0;
    ll i = 1;
    while (i * i <= n) {
        if (n % i == 0) {
            ans += i;
            if (i != n / i) {
                ans += n / i;
            }
        }
        i++;
    }
    cout << ans << endl;
}

int main() {
    solve();
}