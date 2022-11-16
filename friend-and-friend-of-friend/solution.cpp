#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll inf = 9223372036854775807;

void solve() {
	ll n, x, m; cin >> n >> x >> m;
	x--;
	vector<vector<ll>> graph = {};
	for (ll i = 0; i < n; i++) {
		graph.push_back({});
	}
	for (ll i = 0; i < m; i++) {
		ll a, b; cin >> a >> b;
		a--; b--;
		graph.at(a).push_back(b);
		graph.at(b).push_back(a);
	}

	vector<ll> dist = {};
	vector<bool> seen = {};
	for (ll i = 0; i < n; i++) {
		dist.push_back(inf);
		seen.push_back(false);
	}
	dist.at(x) = 0;
	seen.at(x) = true;

	deque<ll> data = {x};
	while (data.size() > 0) {
		ll pos = data.at(0);
		data.pop_front();
		for (ll el: graph[pos]) {
			if (seen.at(el)) {
				continue;
			}
			seen.at(el) = true;
			data.push_back(el);
			if (dist.at(el) == inf) {
				dist.at(el) = dist.at(pos) + 1;
			}
		}
	}

	ll ans = 0;
	for (ll i = 0; i < n; i++) {
		if ((0 <= dist.at(i)) && (dist.at(i) <= 2)) {
			ans++;
		}
	}
	if (graph.at(x).size() == 0) {
		ans = 0;
	}
	
	cout << ans << endl;
}

int main() {
    solve();
}