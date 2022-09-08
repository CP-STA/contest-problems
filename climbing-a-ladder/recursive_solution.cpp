#include <bits/stdc++.h>
#define forn(i, n) for (long long i = 0; i < n; i++)
#define MOD 1000000007
typedef long long ll;
using namespace std;


ll n;
ll m[200000];

ll moves(ll n) {
  if (m[n+3] != -1) {
    return m[n+3];
  } else {
    ll ans;
    if (n >= 1) {
      ans = (moves(n-3) + moves(n-1)) % MOD;
    } else {
      ans = 1;
    }
    m[n+3] = ans;
    return ans; 
  }
}
int main() {
  cin >> n;
  forn(i, 200000) {
    m[i] = -1;
  }
  cout << moves(n) << endl;
}