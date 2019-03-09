#include <iostream>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin>>n;
	int x=n/10;
	int y=n%10;
	int cnt=0;
	while(true){
		int tmp=x+y;
		int num=y*10+tmp%10;
		if(num==n)
		{
			cnt++;
			break;
		}
		x=num/10;
		y=num%10;
		cnt++;
	}
	cout<<cnt<<"\n";
	return 0;
}