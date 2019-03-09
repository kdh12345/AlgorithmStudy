#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string str;
	cin>>str;
	int index;
	for(char i='a';i<='z';i++){
		index=str.find(i);//핵심!!! c언어의 .equals와 유사하다. 찾으면 해당 index아니면 -1을 반환하다.
		printf("%d ",index);
	}
	printf("\n");
	return 0;

}