#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	string s, t; cin >> s >> t;

	map<char, ll> dic_s = {};
	for (ll i = 0; i < s.length(); i++) {
		if (dic_s.find(s.at(i)) == dic_s.end()) {
			dic_s[s.at(i)] = 1;
		}
		else {
			dic_s[s.at(i)]++;
		}
	}

	for (ll i = 0; i < t.length(); i++) {
		dic_s[t.at(i)]--;
	}

	for (auto itr = dic_s.begin(); itr != dic_s.end(); itr++) {
		if ((*itr).second > 0) {
			cout << (*itr).first << " " << (*itr).second << endl;
		}
	}
}


int main() {
    solve();
}