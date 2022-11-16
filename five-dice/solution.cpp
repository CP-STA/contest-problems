# include <bits/stdc++.h>
using namespace std;
typedef long long ll;

/* Authored by Kay Akashi */

void solve() {
	ll n; cin >> n;
	ll cnt = 0;
	for (ll i = 1; i <= 6; i++) {
		for (ll j = 1; j <= 6; j++) {
			for (ll k = 1; k <= 6; k++) {
				for (ll l = 1; l <= 6; l++) {
					for (ll m = 1; m <= 6; m++) {
						if (i + j + k + l + m == n) {
							cnt++;
						}
					}
				}
			}
		}
	}
	cout << cnt << endl;
}

int main () {
	solve();
}