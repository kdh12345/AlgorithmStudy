#include <iostream>
using namespace std;

int main(void){
	int num;
	cin>>num;
	int sum=0;
	for(int i=1;i<=num;i++)
		sum+=i;
	cout<<sum<<'\n';
	return 0;
}