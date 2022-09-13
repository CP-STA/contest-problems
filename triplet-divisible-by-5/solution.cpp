#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

vector<vector<ll>> samples = {};

void solve() {
    ll n; cin >> n;
    vector<ll> a = {};
    for (ll i = 0; i < n; i++) {
        ll el; cin >> el;
        a.push_back(el % 5);
    }

    map<ll, ll> dic = {};
    for (ll i = 0; i < 5; i++) {
        dic[i] = 0;
    }
    for (ll el: a) {
        dic[el]++;
    }

    ll ans = 0;
    for (vector<ll> sample: samples) {
        ll cand = 1;
        map<ll, ll> appear = {};
        for (ll i = 0; i < 5; i++) {
            appear[i] = 0;
        }
        appear[sample.at(0)]++;
        appear[sample.at(1)]++;
        appear[sample.at(2)]++;
        for (ll i = 0; i < 5; i++) {
            if (appear[i] == 1) {
                if (dic[i] >= 1) {
                    cand *= dic[i];
                }
                else {
                    cand *= 0;
                }
            }
            else if (appear[i] == 2) {
                if (dic[i] >= 2) {
                    cand *= dic[i] * (dic[i] - 1) / 2;
                }
                else {
                    cand *= 0;
                }
            }
            else if (appear[i] == 3) {
                if (dic[i] >= 3) {
                    cand *= dic[i] * (dic[i] - 1) * (dic[i] - 2) / 6;
                }
                else {
                    cand *= 0;
                }
            }
        }
        ans += cand;
    }

    cout << ans << endl;
}

int main() {
    for (ll i = 0; i < 5; i++) {
        for (ll j = i; j < 5; j++) {
            for (ll k = j; k < 5; k++) {
                if ((i + j + k) % 5 == 0) {
                    samples.push_back({i, j, k});
                }
            }
        }
    }
    solve();
}