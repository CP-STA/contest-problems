#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<ll> accumulate(vector<ll> li) {
    ll n = li.size();
    if (n == 1) {
        return li;
    }
    else {
        vector<ll> ans = {};
        ans.push_back(li.at(0));
        for (ll i = 0; i < n - 1; i++) {
            ans.push_back(ans.at(i) + li.at(i + 1));
        }
        return ans;
    }
}


void solve() {
    ll n, m, k; cin >> n >> m >> k;
    vector<ll> book = {};
    for (ll i = 0; i < n; i++) {
        book.push_back(0);
    }

    for (ll i = 0; i < m; i++) {
        ll l, r; cin >> l >> r;
        l--; r--;
        book.at(l)++;
        if (r != n - 1) {
            book.at(r + 1)--;
        }
    }

    book = accumulate(book);

    ll cnt = 0;
    for (ll el: book) {
        if (el < k) {
            cnt++;
        }
    }

    cout << cnt << endl;
}


int main() {
    solve();
}