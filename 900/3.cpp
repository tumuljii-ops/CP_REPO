 int n=s.length();
           
             vector<int>ans(n,-5);

             int left=0;

             stack<pair<char,int>>st;

             for(int i=n-1;i>=0;i--){
                 
                    if(s[i]==')'){
                          st.push({')',i});
                    }
                    else{
                         
                         if(st.empty()){
                              ans[i]=-1;
                         }
                         else {
                             pair<char,int>p=st.top();
                             st.pop();

                             ans[i]=p.second;


                         }
                    }
             }

             while(!st.empty()){
                  
                  auto top=st.top();

                  st.pop();

                  int x=top.second;

                  ans[x]=-1;
             }

             int count=0;

             int maxi=0;

             for(int i=0;i<n;i++){
                 
                   if(s[i]=='('){
                       
                        if(ans[i]>=0){
                             count=count+2;
                        }
                   }

                   if(ans[i]==-1){
                        maxi=max(maxi,count);
                        count=0;
                   }
             }

             return max(maxi,count);