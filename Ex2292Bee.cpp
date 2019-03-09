#include <iostream>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	long long n;
	cin>>n;
	int cnt=1;
	for(long long i=1;i<n;){
		long long temp=6*(cnt++);// 6 12 18
		i+=temp;// 2 8 20
	}
	cout<<cnt<<"\n";
	return 0;
}