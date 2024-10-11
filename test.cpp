#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.txt","r",stdin);
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)cin>>a[i];
    int total;
    cin>>total;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if((a[i]+a[j]) ==total){
                cout<<i+1<<" "<<j+1<<endl;
                return 0;
            }
        }
    }
    cout<<-1<<endl;
}