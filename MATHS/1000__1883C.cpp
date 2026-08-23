#include <bits/stdc++.h>
using namespace std;

int main(){
     
     int t;
     cin>>t;

     while(t--){
         
         int n,k;

         cin>>n>>k;

         vector<int>arr(n);

         for(int i=0;i<n;i++){
             cin>>arr[i];
         }

         bool ans=false;

         for(int i=0;i<n;i++){
             
              if(arr[i]%k==0){
                   cout<<0<<'\n';
                   ans=true;
                   break;
              }
         }

         if(ans){
             continue;
         }

         if(k==2){
             
            cout<<1<<'\n';
         }
         else if(k==3){

            int ans=INT_MAX;
              
            for(int i=0;i<n;i++){
                  
                  int rem=arr[i]%3;
                  rem=3-rem;
                  ans=min(ans,rem);
                 
            }
            cout<<ans<<'\n';
         }
         else if(k==4){
             
                int even=0;
               int mini=INT_MAX;

               for(int i=0;i<n;i++){
                     if(arr[i]%2==0){
                         even++;
                     }
                   
                     int rem = arr[i] % 4;
                     mini = min(mini, 4 - rem);
               }

            
               int make_two_evens = max(0, 2 - even);

               cout << min(mini, make_two_evens) << '\n';
              

               
         }
         else if(k==5){
             
              int mini=INT_MAX;

              for(int i=0;i<n;i++){
                 
                   int rem=arr[i]%k;
                   rem=5-rem;

                   mini=min(mini,rem);
              }

              cout<<mini<<'\n';
         }



         
     }

     return 0;
}