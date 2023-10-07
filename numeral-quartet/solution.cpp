#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<ll> ans = {};

void dfs(string s, ll A, ll B, ll C, ll D, ll K) {
    if (static_cast<ll>(s.size()) < K) {
        string s1 = s + (char)(A + 48);
        string s2 = s + (char)(B + 48);
        string s3 = s + (char)(C + 48);
        string s4 = s + (char)(D + 48);
        ans.push_back(stoll(s1));
        ans.push_back(stoll(s2));
        ans.push_back(stoll(s3));
        ans.push_back(stoll(s4));
        dfs(s1, A, B, C, D, K);
        dfs(s2, A, B, C, D, K);
        dfs(s3, A, B, C, D, K);
        dfs(s4, A, B, C, D, K);
    }
}

void solve() {
    ll K, A, B, C, D; cin >> K >> A >> B >> C >> D;
    dfs("", A, B, C, D, K);
    sort(ans.begin(), ans.end());
    for (ll el: ans) {
        cout << el << " ";
    }
    cout << endl;
}

int main() {
    solve();
}