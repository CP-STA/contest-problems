#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */


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


ll power(ll x, ll y) {
	ll ans = 1;
	for (ll i = 0; i < y; i++) {
		ans *= x;
	}
	return ans;
}


ll power_modulo(ll a, ll b, ll M) {
	ll tail = 0;
	vector<ll> sample = {a};
	for (ll i = 0; i <= 70; i++) {
		sample.push_back(sample.at(tail) * sample.at(tail) % M);
		tail++;
	}
	ll taill = 0;
	vector<ll> ep = {1};
	for (ll i = 0; i <= 70; i++) {
		ep.push_back(ep.at(taill) * 2);
		taill++;
	}
	map<ll, ll> dic = {};
	for (ll i = 0; i < sample.size(); i++) {
		dic[ep.at(i)] = sample.at(i);
	}
	string s = bin(b);
	reverse(s.begin(), s.end());
	ll ans = 1;
	for (ll i = 0; i < s.length(); i++) {
		if (s.at(i) != '0') {
			ans *= dic[power(2, i)];
			ans %= M;
		}
	}
	return ans;
}


void solve() {
    ll X, Y; cin >> X >> Y;
    ll mod = 1000000007;

    ll a = 1; 
    for (ll i = 1; i <= X; i++) {
    	a *= i;
    	a %= mod;
    }

    ll b = Y;
    for (ll i = 1; i <= X - Y; i++) {
    	b *= i;
    	b %= mod;
    }

    ll x = power_modulo(b, mod - 2, mod);

    ll ans = a * x % mod;
    cout << ans << endl;
}

int main() {
    solve();
}