#include <bits/stdc++.h>
using namespace std;
#define ll long long


/* Authored by Kay Akashi */


/* slice[l:r] */
string cut(string s, ll l, ll r) {
    string ans = "";
    for (ll i = l; i < r; i++) {
        ans += s.at(i);
    }
    return ans;
}


void solve() {
    ll N; cin >> N;
    vector<vector<string>> formulary = {};
    for (ll i = 0; i < N; i++) {
        string name, onset, duration; cin >> name >> onset >> duration;
        formulary.push_back({name, onset, duration});
    }

    vector<string> onsets = {"rapid", "medium", "slow"};
    vector<string> durations = {"long", "medium", "short"};

    map<vector<string>, vector<string>> dic = {};
    for (string onset: onsets) {
        for (string duration: durations) {
            dic[{onset, duration}] = {};
        }
    }

    for (ll i = 0; i < N; i++) {
        dic[{formulary.at(i).at(1), formulary.at(i).at(2)}].push_back(formulary.at(i).at(0));
    }
    for (auto itr = dic.begin(); itr != dic.end(); itr++) {
        vector<string> drugs = dic[itr -> first];
        sort(drugs.begin(), drugs.end()); 
        dic[itr -> first] = drugs;
    }

    map<vector<string>, string> ans = {};
    for (string onset: onsets) {
        for (string duration: durations) {
            ans[{onset, duration}] = "";
        }
    }

    for (auto itr = dic.begin(); itr != dic.end(); itr++) {
        string line = "";
        for (string el: itr -> second) {
            line += el;
            line += ", ";
        }
        ans[itr -> first] = line;
    }

    for (auto itr = ans.begin(); itr != ans.end(); itr++) {
        if ((itr -> second).length() > 0) {
            ans[itr -> first] = cut(ans[itr -> first], 0, ans[itr -> first].length() - 2);
        }
    }

    ll M; cin >> M;
    for (ll i = 0; i < M; i++) {
        string onset, duration; cin >> onset >> duration;
        if (ans[{onset, duration}] == "") {
            cout << "NONE" << endl;
        }
        else {
            cout << ans[{onset, duration}] << endl;
        }
    }
}

int main() {
    solve();
}