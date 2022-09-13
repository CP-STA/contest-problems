# include <bits/stdc++.h>
using namespace std;
typedef long long ll;

/* Authored by Kay Akashi */

void solve() {
	ll X, Y, Z; cin >> X >> Y >> Z;
	
	ll fare = X + (Z / 1000) * Y;
	cout << fare << endl;
}

int main () {
  solve();
}