#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	ll n; cin >> n;
	string s; cin >> s;

	string t = "";
	for (ll i = 0; i < n; i++) {
		if ((ll)(s.at(i)) <= 90) {
			t += char((ll)(s.at(i)) + 32);
		}
		else {
			t += char((ll)(s.at(i)) - 32);
		}
	}

	cout << t << endl;
}

int main() {
    solve();
}