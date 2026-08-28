#include <bits/stdc++.h>
using namespace std;

int main(){
     
     int t;
     cin>>t;

     while(t--){
         
         long long a,b;
         cin>>a>>b;

         long long max=a+1;

         if(a<b){
            cout<<1<<'\n';
            continue;
         }

         long long d=a;

         long long count1=0;

         
         if(b==1){
            count1++;
             
             while(d!=0){
                 d=d/(b+1);
                 count1++;
             }
         }
         else{
             
             while(d!=0){
                 d=d/b;
                 count1++;
             }
         }

         long long c=b++;

         long long prev=count1
         long long thisone=0;

         d=a;

         while(thisone<prev){

              steps=c-b;
              

              while(d!=0){
                  
                   d=d/c;
                   steps++;
              }

              d=a;
              c=c+1;


              thisone=steps;
             
         }

         cout<<thisone<<'\n';
     }
     
     return 0;
     
}