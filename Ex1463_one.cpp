#include <cstdio>
#include <iostream>
using namespace std;
int count=0;
void One(int n){
	if(n==1)
		return;
	if(n%3==0){
		count+=1;
		One(n/3);
	}else if(n%3!=0&&(n%2!=0||n==10)){
		count+=1;
		One(n-1);
	}else if(n%2==0){
		count+=1;
		One(n/2);
	}
	
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int x;
	cin>>x;
	One(x);
	cout<<count<<"\n";
	return 0;

}