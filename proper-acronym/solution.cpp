#include <string>
#include <iostream>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	ll n; cin >> n;
	string acr = "";
	for (ll i = 0; i < n; i++) {
		string t; cin >> t;
		acr += t.at(0);
	}
	string s; cin >> s;

	if (s == acr) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << endl;
	}
}

int main() {
    solve();
}