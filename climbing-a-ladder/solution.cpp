#include <bits/stdc++.h>
#define forn(i, n) for(ll i = 0; i < n; i++)
#define MOD 1000000007
using namespace std;
typedef long long ll;

/* Authored by Deyao Chen */

ll n;

vector<vector<ll> > M = {{1, 0, 1}, {1, 0, 0}, {0, 1, 0}};
vector<vector<ll> > S;
vector<vector<ll> > mul(vector<vector<ll> > a, vector<vector<ll> > b) {
  vector<vector<ll> > res;
  res.resize(3);
  forn(i, 3) {
    res[i].resize(3, 0);
  }
  forn(i, 3) forn(j, 3) forn(k, 3) {
    res[i][j] = ((a[i][k] * b[k][j] % MOD) + res[i][j]) % MOD;

  }
  return res;
} 

void printM(vector<vector<ll> > a){
  forn(i, a.size()){
    forn(j, a[i].size()) {
      cout << a[i][j] << " ";
    }
    cout << endl;
  }
}

vector<vector<ll> > exp(vector<vector<ll> > a, ll n) {
  if (n == 1) {
    return a;
  }
  if (n % 2 == 0) {
    vector<vector<ll> > b = exp(a, n / 2);
    return mul(b, b);
  } else {
    return mul(a, exp(a, n-1));
  }
}

int main() {
  cin >> n;
  if (n == 1) {
    cout << 2 << endl;
  } else if (n == 2) {
    cout << 3 << endl;
  } else if (n == 3) {
    cout << 4 << endl;
  } else {
    S = exp(M, n-3);
    ll fn = ((S[0][0] * 2) % MOD + S[0][1] + S[0][2]) % MOD;
    ll fn1 = ((S[1][0] * 2) % MOD + S[1][1] + S[1][2]) % MOD;
    ll fn2 = ((S[2][0] * 2) % MOD + S[2][1] + S[2][2]) % MOD; 
    cout << (fn + fn1 + fn2) % MOD << endl;
  }
}