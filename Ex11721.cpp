#include <iostream>
#include <string>
using namespace std;

int main(void){
	string str;
	cin>>str;
	for(int i=0;i<str.length();i++){
		if(i%10==0&&i!=0)
			cout<<"\n";
		cout<<str[i];
	}
	cout<<"\n";
	return 0;
}