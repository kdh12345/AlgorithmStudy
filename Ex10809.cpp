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
		index=str.find(i);//�ٽ�!!! c����� .equals�� �����ϴ�. ã���� �ش� index�ƴϸ� -1�� ��ȯ�ϴ�.
		printf("%d ",index);
	}
	printf("\n");
	return 0;

}