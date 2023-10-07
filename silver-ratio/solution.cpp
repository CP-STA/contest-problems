#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
	double q, d; cin >> q >> d;
	double p = d - q / d;
	cout << round(p) << endl;
}

int main() {
    solve();
}