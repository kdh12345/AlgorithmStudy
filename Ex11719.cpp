#include <iostream>
#include <string>
using namespace std;

int main(void){
	string str;
	for(int i=0;i<100;i++){
		getline(cin,str);//공백도 받아들인다.
		cout<<str<<"\n";
	}
	return 0;
}