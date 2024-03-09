// This is incredibly slow, I'm not sure why because the complexity seems to be correct, there's just some really slow constant terms
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define iPair pair<ll, vector<ll>>

vector<vector<ll>> neighbors(vector<ll> point, vector<vector<ll>> lists);
ll id(vector<ll> point, vector<vector<ll>> lists);
ll distance(vector<ll> point1, vector<ll> point2, vector<vector<ll>> lists);

ll solve(ll K, vector<vector<ll>> lists) {
    priority_queue<iPair, vector<iPair>, greater<iPair>> dq;
    vector<ll> init;
    init.resize(lists.size(), 0);
    dq.push({0, init});
    unordered_map<ll, ll> dist;
    for (ll i = 0; i < K-1; i++) {
        auto [d, v] = dq.top(); dq.pop();
        for (auto neighbor : neighbors(v, lists)) {
            ll alt = d + distance(v, neighbor, lists);
            if (dist.find(id(neighbor, lists)) == dist.end() || alt < dist.at(id(neighbor, lists))) {
                dist[id(neighbor, lists)] = alt;
                dq.push({alt, neighbor});
            }
        }
    }

    auto [d, v] = dq.top(); dq.pop();
    ll ans = 0;
    for (ll i = 0; i < lists.size(); i++) {
        ans += lists.at(i).at(0);
    }
    return ans - d;
}

// because a vector cannot be the key of an unordered_map, we need to convert it to a number
ll id(vector<ll> point, vector<vector<ll>> lists) {
    ll id = 0;
    for (ll i = point.size() - 1; i >= 0; i--) {
        id *= lists.at(i).size();
        id += point.at(i);
    }
    return id;
}

// get neighbors of a point, in the case of the proboem, the two neiboughrs are either moving on to the next most expensive sushi or ramen place.
vector<vector<ll>> neighbors(vector<ll> point, vector<vector<ll>> lists) {
    vector<vector<ll>> n;
    n.reserve(point.size());
    for (ll i = 0; i < point.size(); i++) {
        if (point.at(i) < lists.at(i).size() - 1) {
            vector<ll> p;
            p.resize(point.size());
            for (ll j = 0; j < point.size(); j++) {
                p.at(j) = point.at(j);
            }
            p.at(i)++;
            n.push_back(p);
        }
    }
    return n;
}

// the difference between two sets of meal choices, point1 and point2 are both just two numbes (for the problem), and distance is the difference in price
ll distance(vector<ll> point1, vector<ll> point2, vector<vector<ll>> lists) {
    ll d = 0;
    if (point1.size() != point2.size() || point2.size() != lists.size()) {
        throw runtime_error("Invalid input");
    }
    for (ll i = 0; i < point1.size(); i++) {
        vector<ll> l = lists.at(i);
        d += l.at(point1.at(i)) - l.at(point2.at(i));
    }
    return d;
}

int main(){
    ll N, M, K; cin >> N >> M >> K;
    vector<ll> A;
    for (ll i = 0; i < N; i++) {
        ll j; cin >> j;
        A.push_back(j);
    }
    vector<ll> B;
    for (ll i = 0; i < M; i++) {
        ll j; cin >> j;
        B.push_back(j);
    }
    sort(A.begin(), A.end(), greater<ll>());
    sort(B.begin(), B.end(), greater<ll>());
    vector<vector<ll>> lists = {A, B};
    cout << solve(K, lists) << endl;
}