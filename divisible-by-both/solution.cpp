#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
  ll n, a, b; cin >> n >> a >> b;
  ll LCM = a / gcd(a, b) * b;
  cout << n / LCM << endl;
}

int main() {
    solve();
}