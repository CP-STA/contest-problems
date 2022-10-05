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

void solve() {
	ll n; cin >> n;
	vector<ll> a = import_vector(n);
	sort(a.begin(), a.end());

	map<ll, ll> largest = {};
	map<ll, ll> smallest = {};
	for (ll el: a) {
		largest[el] = -1;
		smallest[el] = n;
	}
	for (ll i = 0; i < n; i++) {
		largest[a.at(i)] = i;
	}
	for (ll i = n - 1; i >= 0; i--) {
		smallest[a.at(i)] = i;
	}

	ll m; cin >> m;
	for (ll i = 0; i < m; i++) {
		ll x; cin >> x;
		string op; cin >> op;

		if (op == "LARGER") {
			bool flag = true;
			ll left = -1;
			ll right = n;
			while (left + 1 < right) {
				ll mid = (left + right) / 2;
				if (a.at(mid) < x) {
					left = mid;
				}
				else if (x < a.at(mid)) {
					right = mid;
				}
				else {
					cout << (n - 1) - (largest[a.at(mid)] + 1) + 1 << endl;
					flag = false;
					break;
				}
			}
			if (flag) {
				if (x < a.at(0)) {
					cout << n << endl;
				}
				else if (a.at(n - 1) <= x) {
					cout << 0 << endl;
				}
				else {
					cout << n - right << endl;
				}
			}
		}
		else {
			bool flag = true;
			ll left = -1;
			ll right = n;
			while (left + 1 < right) {
				ll mid = (left + right) / 2;
				if (a.at(mid) < x) {
					left = mid;
				}
				else if (x < a.at(mid)) {
					right = mid;
				}
				else {
					cout << smallest[a.at(mid)] << endl;
					flag = false;
					break;
				}
			}
			if (flag) {
				if (a.at(n - 1) < x) {
					cout << n << endl;
				}
				else if (x <= a.at(0)) {
					cout << 0 << endl;
				}
				else {
					cout << right << endl;
				}
			}
		}
	}
}

int main () {
	solve();
}