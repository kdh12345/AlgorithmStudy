#include <iostream>
using namespace std;

int main(void){
	int a,b;
	cin>>a>>b;
	if(a<0||b>10)
		return -1;
	cout.precision(10);
	cout<<(double)a/b<<'\n';
	return 0;
}