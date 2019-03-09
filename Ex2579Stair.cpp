
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	int arr[301]={0,};
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>arr[i];
	}
	int m=arr[n];
	for(int i=n-1;i>0;i--){
		m+=max(arr[i],arr[i-1]);
		i--;
	}
	cout<<m<<"\n";
	return 0;
}*/

int main(void){// bottom-up
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin>>n;
	int arr[301]={0,};
	int dp[301]={0,};
	for(int i=1;i<=n;i++){
		cin>>arr[i];
	}
	dp[1]=arr[1];
	if(n>1)
		dp[2]=dp[1]+arr[2];
	for(int i=3;i<=n;i++){
		dp[i]=max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]);
	}
	cout<<dp[n]<<"\n";
	return 0;
}