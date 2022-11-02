#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll smaller(ll a, ll b) {
	if (a <= b) {
		return a;
	}
	else {
		return b;
	}
}

ll larger(ll a, ll b) {
	if (a >= b) {
		return a;
	}
	else {
		return b;
	}
}

vector<ll> import_vector(ll n) {
    vector<ll> li;
    for (ll i = 0; i < n; i++) {
        ll j; cin >> j;
        li.push_back(j);
    }
    return li;
}

void solve() {
	ll n; cin >> n;
	vector<ll> A = import_vector(n);

	ll coin = 0;
	for (ll i = 0; i < n; i++) {
		if (A.at(i) >= 0) {
			coin = smaller(10, coin + A.at(i));
		}
		else {
			coin = larger(0, coin + A.at(i));
		}
	}

	cout << coin << endl;
}


int main() {
    solve();
}