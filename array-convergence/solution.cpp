# include <bits/stdc++.h>
using namespace std;
typedef long long ll;

/* Authored by Kay Akashi */

vector<ll> import_vector(ll n) {
    vector<ll> li;
    for (ll i = 0; i < n; i++) {
        ll j; cin >> j;
        li.push_back(j);
    }
    return li;
}

ll max(vector<ll> li) {
	ll x = li.at(0);
	for (ll el: li) {
		if (el > x) {
			x = el;
		}
	}
	return x;
}

ll min(vector<ll> li) {
	ll x = li.at(0);
	for (ll el: li) {
		if (el < x) {
			x = el;
		}
	}
	return x;
}

void judge(bool x) {
	if (x) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
}

void solve() {
	ll n, k; cin >> n >> k;
	vector<ll> a = import_vector(n);

	ll m = min(a);
	ll M = max(a);

	judge(m + k >= M - k);
}

int main () {
  solve();
}