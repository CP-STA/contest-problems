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

ll smaller(ll a, ll b) {
	if (a <= b) {
		return a;
	}
	else {
		return b;
	}
}

ll inf = 1000000000;

void solve() {
	ll N, T; cin >> N >> T;
	vector<ll> W = import_vector(N);

	vector<vector<ll>> dp = {};
	for (ll i = 0; i <= N; i++) {
		vector<ll> li = {};
		for (ll j = 0; j <= T; j++) {
			li.push_back(inf);
		}
		dp.push_back(li);
	}

	dp.at(0).at(0) = 0;

	for (ll i = 0; i < N; i++) {
		for (ll j = 0; j <= T; j++) {
			if (j - W.at(i) >= 0) {
				dp.at(i + 1).at(j) = smaller(dp.at(i).at(j), dp.at(i).at(j - W.at(i)) + 1);
			}
			else {
				dp.at(i + 1).at(j) = dp.at(i).at(j);
			}
		}
	}

	if (dp.at(N).at(T) != inf) {
		cout << dp.at(N).at(T) << endl;
	}
	else {
		cout << -1 << endl;
	}
}


int main() {
    solve();
}