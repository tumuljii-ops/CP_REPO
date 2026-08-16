#include <bits/stdc++.h>
using namespace std;

int main(){
     
    int t;
    cin>>t;

    while(t--){
       
         int n,k;
         cin>>n>>k;

         string s;
         cin>>s;

         unordered_map<char,int>mpp;

         for(int i=0;i<s.length();i++){
               mpp[s[i]]++;
         }

         if(s.length()==1){
            cout<<"YES"<<'\n';
            continue;
         }

         if(s.length()-k==1){
             cout<<"YES"<<'\n';
             continue;
         }

         vector<int>even;
         vector<int>odd;

         for(auto it:mpp){
               if(it.second%2==0){
                   even.push_back(it.second);
               }
               else{
                   odd.push_back(it.second);
               }
         }

         if(odd.size()==0){
               cout<<"YES"<<'\n';
               continue;
         }
         
         int total_remaining_odd = odd.size() - k;
         
         if(total_remaining_odd > 1){
            cout<<"NO"<<'\n';
         }
         else{
            cout<<"YES"<<'\n';
         }
    }

    return 0;
}