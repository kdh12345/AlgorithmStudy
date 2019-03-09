#include <iostream>
using namespace std;
//int arr[10001]={0,};
//int memo[10030]={0,};
//int index=0;
//int d(int n){//memoization
//	int idx=n;
//	if(n>=10000){//if는 셀프넘버 판별
//		idx+=n/10000;
//		n%=10000;
//	}if(n>=1000){
//		idx+=n/1000;
//		n%=1000;
//	}if(n>=100){
//		idx+=n/100;
//		n%=100;
//	}if(n>=10){
//		idx+=n/10;
//		n%=10;
//	}
//	memo[idx]=idx+n;
//	return memo[idx];
//}
//int main(void){
//	ios_base::sync_with_stdio(false);
//	cout.tie(0);
//	for(int i=1;i<=10000;i++){
//		arr[d(i)]=1;
//		if(arr[i]==0){
//			cout<<i<<"\n";
//		}
//	}
//	return 0;
//}
#include <iostream>
using namespace std;
int arr[10001];
int d(int n){//memoization
	int idx=n;
	while(1){
        if(n==0)
            break;
        idx+=n%10;
        n/=10;
    }//셀프넘버 판별!!!!
	return idx;
	
}
int main(void){
	ios_base::sync_with_stdio(false);
	cout.tie(0);
	for(int i=1;i<=10000;i++){
		arr[d(i)]=1;
		if(arr[i]==0){
			cout<<i<<"\n";
		}
	}
	return 0;
}