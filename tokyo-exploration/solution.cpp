#include <bits/stdc++.h>
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
    ll N, M, K; cin >> N >> M >> K;
    vector<ll> A = import_vector(N);
    vector<ll> B = import_vector(M);
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    set<vector<ll>> seen = {{N - 1, M - 1}};
    multiset<vector<ll>> S = {{A.at(N - 1) + B.at(M - 1), N - 1, M - 1}};
    vector<ll> price = {};
    while (price.size() < K) {
        vector<ll> M = *S.rbegin();
        S.erase(S.find(M));
        price.push_back(M.at(0));
        ll I = M.at(1);
        ll J = M.at(2);
        if (I > 0) {
            if (seen.find({I - 1, J}) == seen.end()) {
                S.insert({A.at(I - 1) + B.at(J), I - 1, J});
                seen.insert({I - 1, J});
            }
        }
        if (J > 0) {
            if (seen.find({I, J - 1}) == seen.end()) {
                S.insert({A.at(I) + B.at(J - 1), I, J - 1});
                seen.insert({I, J - 1});
            }
        }
    }

    cout << price.at(K - 1) << endl;
}


int main() {
    solve();
}