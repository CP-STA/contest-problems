#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	ll g, y, r, t; cin >> g >> y >> r >> t;
	if (t != 86400) {
		t %= (g + 2 * y + r);
		if (0 <= t && t < g) {
			cout << "green" << endl;
		}
		else if (g <= t && t < g + y) {
			cout << "yellow" << endl;
		}
		else if (g + y <= t && t < g + y + r) {
			cout << "red" << endl;
		}
		else if (g + y + r <= t && t < g + 2 * y + r) {
			cout << "yellow" << endl;
		}
	}
	else {
		cout << "green" << endl;
	}
}


int main() {
    solve();
}