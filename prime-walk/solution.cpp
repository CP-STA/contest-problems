#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<ll> get_prime(ll N) {
    vector<bool> sample = {};
    for (ll i = 0; i <= N; i++) {
        sample.push_back(true);
    }
    sample.at(0) = false;
    sample.at(1) = false;
    ll head = pow(N, 0.5) + 1;
    for (ll i = 2; i <= head; i++) {
        ll v = 2;
        while (true) {
            if (i * v > N) {
                break;
            }
            sample.at(i * v) = false;
            v++;
        }
    }
    vector<ll> ans = {};
    for (ll i = 0; i <= N; i++) {
        if (sample.at(i)) {
            ans.push_back(i);
        }
    }
    return ans;
}

ll total(vector<ll> li) {
    ll ans = 0;
    for (ll i = 0; i < li.size(); i++) {
        ans += li.at(i);
    }
    return ans;
}


void solve() {
    ll n; cin >> n;
    ll ans = n * (n + 1) / 2 - total(get_prime(n)) * 2;

    cout << ans << endl;
}

int main() {
    solve();
}