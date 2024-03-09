#include <bits/stdc++.h>
using namespace std;
#define ll long long

/* Authored by Kay Akashi */

ll Kx;
ll Ky;
ll Lx;
ll Ly;

bool annoying(vector<ll> A, vector<ll> B) {
    ll Ax = A.at(0);
    ll Ay = A.at(1);
    ll Bx = B.at(0);
    ll By = B.at(1);

    bool flag1 = false;
    ll S11 = Lx * Ay - Ly * Ax; // △OLA
    ll S12 = Lx * By - Ly * Bx; // △OLB
    if (S11 * S12 < 0) {
        flag1 = true;
    }

    bool flag2 = false;
    ll S21 = (Bx - Ax) * (-Ay) - (By - Ay) * (-Ax); // △ABO
    ll S22 = (Bx - Ax) * (Ly - Ay) - (By - Ay) * (Lx - Ax); // △ABL
    if (S21 * S22 < 0) {
        flag2 = true;
    }

    bool flag3 = false;
    if (Lx * Ay == Ly * Ax && abs(Ax) < abs(Lx)) { // if A is standing between Kay and Liana
        flag3 = true;
    }
    if (Lx * By == Ly * Bx && abs(Bx) < abs(Lx)) { // if B is standing between Kay and Liana
        flag3 = true;
    }
    if (Ax * By == Ay * Bx && (Ax * Bx < 0 || Ay * By < 0)) { // if Kay is standing between A and B
        flag3 = true;
    }
    if ((Ly - Ay) * (Bx - Lx) == (Lx - Ax) * (By - Ly) && ((Lx - Ax) * (Lx - Bx) < 0 || (Ly - Ay) * (Ly - By) < 0)) { // if Liana is standing between A and B
        flag3 = true;
    }

    return ((flag1 && flag2) || flag3);
}

void solve() {
    ll N; cin >> N;
    cin >> Kx >> Ky >> Lx >> Ly;
    Lx -= Kx; Ly -= Ky;
    vector<vector<ll>> li = {};
    for (ll i = 0; i < N; i++) {
        ll X, Y; cin >> X >> Y;
        X -= Kx; Y -= Ky;
        li.push_back({X, Y});
    }

    ll cnt = 0;
    for (ll i = 0; i < N - 1; i++) {
        for (ll j = i + 1; j < N; j++) {
            if (annoying(li.at(i), li.at(j)) == true) {
                cnt++;
            }
        }
    }
    cout << cnt << endl;
}


int main() {
    solve();
}