#include <string>
#include <iostream>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<ll> import_vector(ll n) {
    vector<ll> li;
    for (ll i = 0; i < n; i++) {
        ll j; cin >> j;
        li.push_back(j);
    }
    return li;
}

void solve() {
    ll n; cin >> n;
    vector<ll> a = import_vector(n);
    vector<ll> b = import_vector(n);

    set<ll> s = {};
    for (ll el: a) {
        s.insert(el);
    }

    ll cnt = 0;
    for (ll el: b) {
        if (s.find(el) != s.end()) {
            cnt++;
        }
    }
    cout << cnt << endl;
}

int main() {
    solve();
}