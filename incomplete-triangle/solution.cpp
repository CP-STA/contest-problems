#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll larger(ll a, ll b) {
	if (a >= b) {
		return a;
	}
	else {
		return b;
	}
}

void solve() {
	ll r, g, b; cin >> r >> g >> b;
	vector<ll> li = {r, g, b};
	sort(li.begin(), li.end());
	r = li.at(0);
	g = li.at(1);
	b = li.at(2);

	ll ans = larger(b + 1 - r - g, 0);
	cout << ans << endl;
}

int main() {
    solve();
}