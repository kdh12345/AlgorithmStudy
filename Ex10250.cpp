#include <iostream>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int h,w,n;
	int num1=0;
	int num2=0;
	for(int i=0;i<t;i++){
		cin>>h>>w>>n;
		if(n%h!=0)
		{
			num1=n%h;
			num2=n/h+1;
			if(num2>=10)
				cout<<num1<<num2<<"\n";
			else
				cout<<num1<<0<<num2<<"\n";
		}	
		else if(n%h==0){
			num1=h;
			num2=n/h;
			if(num2>=10)
				cout<<num1<<num2<<"\n";
			else
				cout<<num1<<0<<num2<<"\n";
		}
		
	}
	return 0;
}