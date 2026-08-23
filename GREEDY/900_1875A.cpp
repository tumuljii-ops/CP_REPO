#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        long long a, b, n;
        cin >> a >> b >> n;

        // FIXED: Initialize vector size n
        vector<long long> ans(n);

        for (int i = 0; i < n; i++) {
            cin >> ans[i];
        }

        // Start with the initial timer value 'b'
        long long total = b;

        // Greedy Math: Each tool x_i adds min(x_i, a - 1) seconds to total survival time
        for (int i = 0; i < n; i++) {
            total += min(ans[i], a - 1);
        }

        cout << total << '\n';
    }

    return 0;
}