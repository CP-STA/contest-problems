#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<ll> import_vector(ll n) {
    vector<ll> li;
    for (ll i = 0; i < n; i++) {
        ll j; cin >> j;
        li.push_back(j);
    }
    return li;
}

ll lcm(ll a, ll b) {
	return a / gcd(a, b) * b;
}

void solve() {
	ll n, X; cin >> n >> X;
	vector<ll> a = import_vector(n);

	bool exceed = false;
	ll p = a.at(0);
	for (ll i = 0; i < n; i++) {
		p = lcm(p, a.at(i));
		if (p > X) {
			break;
			exceed = true;
		}
	}

	if (p > X || exceed) {
		cout << -1 << endl;
	}
	else {
		cout << (X / p) * p << endl;
	}
}

int main() {
    solve();
}