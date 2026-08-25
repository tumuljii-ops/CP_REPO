#include <bits/stdc++.h>
using namespace std;

int main(){
     
    
         
        int n;
        cin>>n;

        string s;
        cin>>s;

        int l=n-1;

        while(l>=1 && s[l]>=s[l-1]){
             
               l--;
        }

        if(l==0){
            cout<<"NO"<<'\n';
            return 0;
        }

        cout<<"YES"<<'\n';
        cout<<l<<" "<<l+1<<'\n';
        

        

    return 0;
}