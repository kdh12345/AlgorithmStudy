#include <iostream>
#include <vector>
using namespace std;
int gcd(int a,int b){
	while(b!=0){
		int r=a%b;
		a=b;
		b=r;
	}
	return a;
}
int lcm(int a,int b){
	return a*b/gcd(a,b);
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin>>t;
	vector<int> v;
	for(int i=0;i<t;i++){
		int m,n,x,y;
		cin>>m>>n>>x>>y;
		int cnt=
		v.push_back(cnt);
	}
	for(int i=0;i<v.size();i++)
		cout<<v[i]<<"\n";
	return 0;
}