#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll inf = 9223372036854775807;

vector<ll> dijkstra(vector<vector<vector<ll>>> graph, ll N, ll s) {
    vector<ll> dist = {}; for (ll i = 0; i < N; i++) {
        dist.push_back(inf);
    }
    dist.at(s) = 0;
    priority_queue<vector<ll>, vector<vector<ll>>, greater<vector<ll>>> data = {};
    data.push({0, s});
    while (data.size() > 0) {
        ll pos = data.top().at(1);
        data.pop();
        for (vector<ll> el: graph.at(pos)) {
            ll node = el.at(0); ll cost = el.at(1);
            if (dist.at(pos) + cost < dist.at(node)) {
                dist.at(node) = dist.at(pos) + cost;
                data.push({dist.at(node), node});
            }
        }
    }
    return dist;
}

ll larger(ll a, ll b) {
    if (a >= b) {
        return a;
    }
    else {
        return b;
    }
}

void solve() {
    ll N; cin >> N;
    vector<vector<vector<ll>>> graph = {};
    for (ll i = 0; i < N; i++) {
        graph.push_back({});
    }
    for (ll i = 0; i < N - 1; i++) {
        ll A, B, C; cin >> A >> B >> C;
        A--; B--;
        graph.at(A).push_back({B, C});
        graph.at(B).push_back({A, C});
    }

    vector<ll> dist = dijkstra(graph, N, 0);
    ll farthest_index = -inf;
    ll farthest_distance = -inf;
    for (ll i = 0; i < N; i++) {
        if (farthest_distance <= dist.at(i)) {
            farthest_distance = dist.at(i);
            farthest_index = i;
        }
    }

    ll ans = -inf;
    vector<ll> dist_2 = dijkstra(graph, N, farthest_index);
    for (ll i = 0; i < N; i++) {
        ans = larger(ans, dist_2.at(i));
    }

    cout << ans << endl;
}

int main() {
    solve();
}