#include <cstdio>
#include <iostream>
using namespace std;

int main(void)
{
	long a,b,c; ///21�� ������ �ڿ��� ǥ������
	scanf("%ld %ld %ld",&a,&b,&c);
	if(b>=c)
	{
		printf("-1\n");
	}else
		printf("%d\n",a/(c-b)+1);
	return 0;

}