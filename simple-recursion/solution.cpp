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

ll power(ll x, ll y) {
    ll ans = 1;
    for (ll i = 0; i < y; i++) {
        ans *= x;
    }
    return ans;
}


void solve() {
    ll p, q, X; cin >> p >> q >> X;
    ll mod = 1000000007;

    vector<vector<vector<ll>>> li = {{{p, q}, {0, 1}}};
    for (ll i = 0; i < 50; i++) {
        vector<vector<ll>> M = li.at(li.size() - 1);
        li.push_back(matrix_multiplication_modulo(M, M, mod));
    }

    string s = bin(X - 1);
    reverse(s.begin(), s.end());

    vector<vector<ll>> ans = {{1}, {1}};
    for (ll i = 0; i < s.size(); i++) {
        if (s.at(i) == '1') {
            ans = matrix_multiplication_modulo(li.at(i), ans, mod);
        }
    }

    cout << ans.at(0).at(0) << endl;
}


int main() {
    solve();
}