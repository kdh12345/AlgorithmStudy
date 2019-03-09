#include <iostream>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin>>n;
	int dp[10001]={0,};
	int arr[10001]={0,};
	for(int i=1;i<=n;i++){
		int num;
		cin>>num;
		arr[i]=num;
	}
	dp[1]=arr[1];
	if(n>1)
		dp[2]=dp[1]+arr[2];
	for(int i=3;i<=n;i++){
		dp[i]=max(dp[i-3]+arr[i-1]+arr[i],dp[i-3]+arr[i]+arr[i-2]);
	}
	cout<<dp[n]<<"\n";
	return 0;
}