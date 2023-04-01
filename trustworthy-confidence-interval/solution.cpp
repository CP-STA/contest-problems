#include <bits/stdc++.h>
#include <cmath>
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

vector<double> import_vector(ll n) {
    vector<double> li;
    for (ll i = 0; i < n; i++) {
        ll j; cin >> j;
        li.push_back(j);
    }
    return li;
}

void show(vector<ll> li) {
    if (li.size() > 0) {
        for (ll i = 0; i < li.size() - 1; i++) {
            cout << li.at(i) << " ";
        }
        cout << li.at(li.size() - 1) << endl;
    }
    else {
        cout << " " << endl;
    }
}

ll smaller(ll a, ll b) {
    if (a <= b) {
        return a;
    }
    else {
        return b;
    }
}

ll larger(ll a, ll b) {
    if (a >= b) {
        return a;
    }
    else {
        return b;
    }
}

double total(vector<double> li) {
    double ans = 0;
    for (double el: li) {
        ans += el;
    }
    return ans;
}

void solve() {
    ll N, L; cin >> N >> L;
    vector<double> A = import_vector(N);

    vector<vector<double>> caterpillar = {}; /* sum(X_i^{2}), sum(X_i) */

    double s = 0;
    double sq = 0;
    for (ll i = 0; i < L; i++) {
        s += A.at(i);
        sq += pow(A.at(i), 2);
    }
    caterpillar.push_back({sq, s});

    for (ll i = 0; i < N - L; i++) {
        vector<double> head = {};
        head.push_back(caterpillar.at(caterpillar.size() - 1).at(0) + pow(A.at(i + L), 2) - pow(A.at(i), 2));
        head.push_back(caterpillar.at(caterpillar.size() - 1).at(1) + A.at(i + L) - A.at(i));
        caterpillar.push_back(head);
    }

    vector<vector<ll>> CI = {};
    for (vector<double> sample: caterpillar) {
        double lower = sample.at(1) / L - 1.96 * pow(sample.at(0) / L - pow(sample.at(1) / L, 2), 0.5);
        double upper = sample.at(1) / L + 1.96 * pow(sample.at(0) / L - pow(sample.at(1) / L, 2), 0.5);
        ll lower_int = max((ll)ceil(lower), 0LL);
        ll upper_int = min((ll)floor(upper), 1000LL);
        CI.push_back({lower_int, upper_int});
    }

    vector<ll> ans = {};
    for (ll i = 0; i < 1002; i++) {
        ans.push_back(0);
    }
    for (vector<ll> ci: CI) {
        ans.at(ci.at(0))++;
        ans.at(ci.at(1) + 1)--;
    }
    ans = accumulate(ans);
    ans.pop_back();

    show(ans);
}

int main() {
    solve();
}