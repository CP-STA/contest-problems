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


vector<vector<ll>> matrix_multiplication_modulo(vector<vector<ll>> A, vector<vector<ll>> B, ll mod) {
	ll a = A.size();
	ll b = A.at(0).size();
	ll c = B.at(0).size();
	vector<vector<ll>> M = {};
	for (ll i = 0; i < a; i++) {
		M.push_back({});
	}
	for (ll i = 0; i < a; i++) {
		for (ll k = 0; k < c; k++) {
			M.at(i).push_back(0);
		}
	}
	for (ll i = 0; i < a; i++) {
		for (ll k = 0; k < c; k++) {
			ll s = 0;
			for (ll j = 0; j < b; j++) {
				s += A.at(i).at(j) * B.at(j).at(k);
				s %= mod;
			}
			M.at(i).at(k) = s;
		}
	}
	return M;
} 


string bin(ll n) {
	string ans = "";
	ll head = n;
	while (head > 0) {
		ans += to_string(head % 2);
		head = head / 2;
	}
	reverse(ans.begin(), ans.end());
	return ans;
}


string zfill(string s, ll n) {
	string t = "";
	for (ll i = s.length() - 1; i > -1; i--) {
		t += s.at(i);
	}
	for (ll i = 0; i < n - s.length(); i++) {
		t += '0';
	}
	reverse(t.begin(), t.end());
	return t;
}


void solve() {
	ll p, q, r; cin >> p >> q >> r;
	ll x, y, z; cin >> x >> y >> z;
	ll k; cin >> k;

	ll mod = 1000000009;

	vector<vector<ll>> M = {{p, q, r}, {1, 0, 0}, {0, 1, 0}};

	map<ll, vector<vector<ll>>> dic = {};
	for (ll i = 0; i < 60; i++) {
		dic[power(2, i)] = {};
	}
	dic[1] = M;
	for (ll i = 1; i < 60; i++) {
		dic[power(2, i)] = matrix_multiplication_modulo(dic[power(2, i - 1)], dic[power(2, i - 1)], mod);
	}

	string snippet = zfill(bin(k - 1), 60);
	reverse(snippet.begin(), snippet.end());

	vector<vector<ll>> MX = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
	for (ll i = 0; i < 60; i++) {
		if (snippet.at(i) == '1') {
			MX = matrix_multiplication_modulo(MX, dic[power(2, i)], mod);
		}
	}

	ll ans = MX.at(2).at(0) * x % mod + MX.at(2).at(1) * y % mod + MX.at(2).at(2) * z % mod;
	ans %= mod;

	cout << ans << endl;
}


int main () {
	solve();
}