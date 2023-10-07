#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	ll N; cin >> N;
	ll ans = 0;
	if (N % 2 == 1) {
		ll g = N / 2 + 1;
		if (g % 2 == 1) {
			ans = 1;
		}
	}
	else {
		ll g = N / 2;
		if (g % 2 == 1) {
			ans = 1;
		}
		ans ^= N;
	}
	ans ^= 0;
	cout << ans << endl;
}

int main() {
    solve();
}