#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

void solve() {
  ll n; cin >> n;
  vector<string> s = {};
  for (ll i = 0; i < n; i++) {
    string t; cin >> t;
    s.push_back(t);
  }
  sort(s.begin(), s.end());
  cout << s.at(0) << endl;
}

int main() {
    solve();
}