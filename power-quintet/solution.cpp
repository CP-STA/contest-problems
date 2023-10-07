# include <bits/stdc++.h>
using namespace std;
typedef long long ll;

/* Authored by Kay Akashi */

ll power(ll x, ll y) {
	ll ans = 1;
	for (ll i = 0; i < y; i++) {
		ans *= x;
	}
	return ans;
}

void solve() {
	ll N; cin >> N;
	bool flag = false;
	for (ll a = 0; a <= 7; a++) {
		for (ll b = 0; b <= 7; b++) {
			for (ll c = 0; c <= 7; c++) {
				for (ll d = 0; d <= 7; d++) {
					for (ll e = 0; e <= 7; e++) {
						if (power(a, a) + power(b, b) + power(c, c) + power(d, d) + power(e, e) == N) {
							flag = true;
						}
					}
				}
			}
		}
	}
	if (flag) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
}

int main () {
		solve();
}