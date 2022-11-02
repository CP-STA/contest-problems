#define MAXN 100000
#include <iostream>
typedef long long ll;
using namespace std;
#define forn(i, n) for(ll i = 0; i< n; i++)

ll p[2*MAXN] = {0};

ll N, M, K, l, r;
void modify(ll l, ll r, ll value) {
    l += N; 
    r += N;
    for(; l < r; l >>= 1, r >>= 1) {
        if (l&1) {p[l++] += value;}
        if (r&1) {p[--r] += value;}
    }
}

int query(ll j) {
    ll res = 0;
    for(j += N; j > 0; j >>= 1) {res += p[j];}
    return res;
}

void push() {
    for (ll i = 1; i < N; i++) {
        p[i<<1] += p[i];
        p[i<<1|1] += p[i];
        p[i] = 0;
    }
}

int main() {
    cin >> N >> M;
    forn(_, M) {
        cin >> l >> r;
        l--;
        modify(l, r, 1);
    }
    push();
    ll ans = 0;
    for(ll i = N; i < 2*N; i++) {
        if (p[i] == 0) ans += 1;
    }
    cout << ans << endl;
}