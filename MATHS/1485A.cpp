#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        long long a, b;
        cin >> a >> b;

        // Base case: If a < b, 1 division brings 'a' to 0
        if(a < b){
            cout << 1 << '\n';
            continue;
        }

        // Store original b to calculate increment steps
        long long orig_b = b;
        long long min_ops = a + 2; // Upper bound (at most a+1 steps)

        // Try small increments of b (incrementing b up to ~30 times is always enough)
        for(long long add = 0; add <= 30; add++){
            long long current_b = orig_b + add;
            
            // Cannot divide by 0 or 1 safely without infinite loops
            if(current_b <= 1){
                continue; 
            }

            long long d = a;
            long long steps = add; // Operations spent incrementing b

            while(d > 0){
                d /= current_b;
                steps++;
            }

            min_ops = min(min_ops, steps);
        }

        cout << min_ops << '\n';
    }

    return 0;
}