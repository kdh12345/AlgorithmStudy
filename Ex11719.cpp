#include <iostream>
#include <string>
using namespace std;

int main(void){
	string str;
	for(int i=0;i<100;i++){
		getline(cin,str);//���鵵 �޾Ƶ��δ�.
		cout<<str<<"\n";
	}
	return 0;
}