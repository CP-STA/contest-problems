#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	string s; cin >> s; ll n = s.length();
	vector<char> ans = {};
	ll L = 0;

	for (ll i = 0; i < n; i++) {
		ans.push_back(s.at(i));
		L += 1;
		if (3 <= L && L < 5) {
			if (ans.at(L - 3) == 'k' && ans.at(L - 2) == 'a' && ans.at(L - 1) == 'y') {
				ans.pop_back(); ans.pop_back(); ans.pop_back();
				L -= 3;
			}
		}
		else if (5 <= L) {
			if (ans.at(L - 3) == 'k' && ans.at(L - 2) == 'a' && ans.at(L - 1) == 'y') {
				ans.pop_back(); ans.pop_back(); ans.pop_back();
				L -= 3;
			}
			else if (ans.at(L - 5) == 'd' && ans.at(L - 4) == 'e' && ans.at(L - 3) == 'y' && ans.at(L - 2) == 'a' && ans.at(L - 1) == 'o') {
				ans.pop_back(); ans.pop_back(); ans.pop_back(); ans.pop_back(); ans.pop_back();
				L -= 5;
			}
		}
	}

	string t = "";
	for (ll i = 0; i < ans.size(); i++) {
		t += ans.at(i);
	}

	cout << t << endl;
}

int main() {
    solve();
}