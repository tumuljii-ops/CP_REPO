#include <bits/stdc++.h>
using namespace std;

int main(){
     
     int t;
     cin>>t;

     while(t--){
         
         long long n;
         cin>>n;


         if(n==1){
             cout<<1<<'\n';
             continue;
         }
         else if(n%3!=0){
             cout<<-1<<'\n';
             continue;
         }

         bool ans=true;

         int steps=0;

         while(n!=1){
             
             if(n%6==0){
                 n=n/6;
                 steps++;
             }
             else{
                 
                n=n*2;
                if(n%3!=0){
                     ans=false;
                     break;
                }
                steps++;
             }
         }

         if(ans){
            cout<<steps<<'\n';
         }
         else{
            cout<<-1<<'\n';
         }
     }

     return 0;
}