#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	ll a1, b1, c1, a2, b2, c2; cin >> a1 >> b1 >> c1 >> a2 >> b2 >> c2;
	ll p = a2 - a1;
	ll q = b2 - b1;
	ll r = c2 - c1;
	if (q * q - 4 * r < 0) {
		cout << endl;
	}
	else {
		ll left = (-q - pow(q * q - 4 * r, 0.5)) / (2 * p);
		ll right = (-q + pow(q * q - 4 * r, 0.5)) / (2 * p);
		vector<ll> ans = {};
		for (ll x = left - 3; x < right + 1 + 3; x++) {
			if (a2 * x * x + b2 * x + c2 != 0) {
				if ((a1 * x * x + b1 * x + c1) % (a2 * x * x + b2 * x + c2) == 0 && (a1 * x * x + b1 * x + c1) / (a2 * x * x + b2 * x + c2) > 0) {
					ans.push_back(x);
				}
			}
		}
		for (ll x: ans) {
			cout << x << " ";
		}
		cout << endl;
	}
}

int main() {
    solve();
}