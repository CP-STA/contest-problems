#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */


class UnionFind {
    public:
    vector <ll> par;
    vector <ll> siz;
    UnionFind(ll N): par(N), siz(N, 1) {
        for (ll i = 0; i < N; i++)  par[i] = i;
    }
    void init(ll N) {
        par.resize(N);
        siz.assign(N, 1);
        for (ll i = 0; i < N; i++) par[i] = i;
    }
    ll root(ll x) {
        while (par[x] != x) {
            x = par[x] = par[par[x]];
        }
        return x;
    }
    ll magnitude(ll x) {
        return siz[root(x)];
    }
    bool unite(ll x, ll y) {
        x = root(x);
        y = root(y);
        if (x == y) return false;
        if (siz[x] < siz[y]) swap(x, y);
        siz[x] += siz[y];
        par[y] = x;
        return true;
    }
};


void solve() {
    ll N; cin >> N;
    UnionFind uf(N);
    ll M1; cin >> M1;
    for (ll i = 0; i < M1; i++) {
        ll u, v; cin >> u >> v;
        u--; v--;
        uf.unite(u, v);
    }
    ll M2; cin >> M2;
    ll cnt = 0;
    for (ll i = 0; i < M2; i++) {
        ll u, v; cin >> u >> v;
        u--; v--;
        if (uf.root(u) == uf.root(v)) {
            cnt++;
        }
    }
    cout << cnt << endl;
}


int main() {
    solve();
}