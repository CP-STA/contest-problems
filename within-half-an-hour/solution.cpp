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


void solve() {
	ll n, m, s; cin >> n >> m >> s;
	s--;
	vector<vector<vector<ll>>> graph = {};
	for (ll i = 0; i < n; i++) {
  	    graph.push_back({});
  	}
    for (ll i = 0; i < m; i++) {
  	    ll a, b, c; cin >> a >> b >> c;
  	    a--; b--;
  	    graph.at(a).push_back({b, c});
  	    graph.at(b).push_back({a, c});
    }

    vector<ll> dist = dijkstra(graph, n, s);

    ll cnt = 0;
    for (ll i = 0; i < dist.size(); i++) {
    	if (dist.at(i) <= 30) {
    		cnt++;
    	}
    }

    cout << cnt << endl;
}


int main() {
    solve();
}