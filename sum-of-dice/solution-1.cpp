#define MOD 7340033
#include <vector>
#include <iostream>
typedef long long ll;
using namespace std;

void print_vector(vector<ll> v){
    for (ll a : v){
        cout << a << " ";
    }
    cout << endl;
}

vector<ll> polynomial_mul(vector<ll> a, vector<ll> b, ll modulus, ll k){
    vector<ll> c;
    c.resize(k, 0);
    for (ll i = 0; i < a.size(); i++){
        for (ll j = 0; j < b.size(); j++){
            if (i + j < k){
                c[i + j] = (c[i + j] + a[i] * b[j]) % modulus;
            }
        }
    }
    return c;
}

vector<ll> polynomial_pow(vector<ll> coefficients, ll n, ll modulus, ll k){
    if (n == 0) {
        return {1};
    }
    if (n % 2 == 0){
        auto ans = polynomial_pow(polynomial_mul(coefficients, coefficients, modulus, k), n / 2, modulus, k);
        auto first = ans.begin();
        auto last = ans.begin() + k;
        vector<ll> newVec(first, last);
        return newVec;
    }
    else{
        auto ans = polynomial_mul(coefficients, polynomial_pow(coefficients, n - 1, modulus, k), modulus, k);
        auto first = ans.begin();
        auto last = ans.begin() + k;
        vector<ll> newVec(first, last);
        return newVec;
    }
}

int main(){
    ll n, k;
    cin >> n >> k;
    vector<ll> ans = polynomial_pow({1, 1, 1, 1, 1, 1}, n, MOD, k);
    for (ll a : ans) {
        cout << a << " ";
    }
    cout << endl;
}