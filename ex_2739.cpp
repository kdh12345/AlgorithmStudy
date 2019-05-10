#include <iostream>
using namespace std;

int main(void){
	int gu;
	cin>>gu;
	for(int i=1;i<10;i++){
		cout<<gu<<' '<<'*'<<' '<<i<<' '<<'='<<' '<<gu*i<<'\n';
	}
	return 0;
}