#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
    ll N, M, C; cin >> N >> M >> C;
    vector<ll> P = {};
    for (ll i = 0; i < C; i++) {
        ll p; cin >> p;
        p--;
        P.push_back(p);
    }

    vector<vector<ll>> graph = {};
    for (ll i = 0; i < N; i++) {
        graph.push_back({});
    }
    for (ll i = 0; i < M; i++) {
        ll x, y; cin >> x >> y;
        x--; y--;
        graph.at(x).push_back(y);
        graph.at(y).push_back(x);
    }

    ll inf = 9223372036854775807;

    deque<ll> data = {};
    for (ll p: P) {
        data.push_back(p);
    }
    vector<ll> dist = {};
    for (ll i = 0; i < N; i++) {
        dist.push_back(inf);
    }
    for (ll p: P) {
        dist.at(p) = 0;
    }
    while (data.size() > 0) {
        ll pos = data.at(0);
        data.pop_front();
        for (ll el: graph.at(pos)) {
            if (dist.at(el) == inf) {
                dist.at(el) = dist.at(pos) + 1;
                data.push_back(el);
            }
        }
    }
    for (ll i = 0; i < N; i++) {
        if (dist.at(i) == inf) {
            dist.at(i) = -1;
        }
    }
    for (ll el: dist) {
        cout << el << " ";
    }
    cout << endl;
}

int main() {
    solve();
}