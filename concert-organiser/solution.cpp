# include <bits/stdc++.h>
using namespace std;
typedef long long ll;

/* Authored by Kay Akashi */

void solve() {
	ll N, M; cin >> N >> M;
	vector<vector<ll>> info = {};
	vector<vector<ll>> graph = {};
	vector<ll> outdeg = {};
	for (ll i = 0; i < N; i++) {
		graph.push_back({});
		outdeg.push_back(0);
	}
	for (ll i = 0; i < M; i++) {
		ll P, Q; cin >> P >> Q;
		P--; Q--;
		graph.at(Q).push_back(P);
		info.push_back({P, Q});
		outdeg.at(P)++;
	}
	deque<ll> sink = {};
	for (ll i = 0; i < N; i++) {
		if (outdeg.at(i) == 0) {
			sink.push_back(i);
		}
	}
	deque<ll> ans = {};
	while (sink.size() > 0) {
		ll pos = sink.at(0);
		ans.push_front(pos);
		sink.pop_front();
		for (ll el: graph.at(pos)) {
			outdeg.at(el)--;
			if (outdeg.at(el) == 0) {
				sink.push_back(el);
			}
		}
	}
	map<ll, ll> ind = {};
	for (ll i = 0; i < ans.size(); i++) {
		ind[ans.at(i)] = i;
	}

	if (ans.size() < N) {
		cout << "No" << endl;
	}
	else {
		bool flag = true;
		for (vector<ll> el: info) {
			ll P = el.at(0);
			ll Q = el.at(1);
			if (ind[P] > ind[Q]) {
				flag = false;
				break;
			}
		}
		if (flag) {
			cout << "Yes" << endl;
		}
		else {
			cout << "No" << endl;
		}
	}
}

int main () {
	solve();
}