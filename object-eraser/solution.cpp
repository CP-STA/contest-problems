#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<ll> accumulate(vector<ll> A) {
    ll N = A.size();
    if (N == 0) {
        return {};
    }
    else if (N == 1) {
        return {A.at(0)};
    }
    else {
        vector<ll> acc = {A.at(0)};
        for (ll i = 1; i < N; i++) {
            acc.push_back(acc.at(i - 1) + A.at(i));
        }
        return acc;
    }
}

vector<ll> import_vector(ll n) {
    vector<ll> li;
    for (ll i = 0; i < n; i++) {
        ll j; cin >> j;
        li.push_back(j);
    }
    return li;
}

void solve() {
    ll N, K; cin >> N >> K;
    vector<ll> A = import_vector(N);

    reverse(A.begin(), A.end());
    vector<ll> acc = accumulate(A);
    ll cnt = 0;
    for (ll i = 0; i < N; i++) {
        if (acc.at(i) <= K) {
            cnt = i + 1;
        }
    }
    cout << cnt << endl;
}


int main() {
    solve();
}