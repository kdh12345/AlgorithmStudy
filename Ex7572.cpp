#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main(void)
{
	char c[15]="ABCDEFGHIJKL";
	char b[15]="01234567890";
	int year;
	scanf("%d",&year);
	year+=56;
	int cycle=(year)%60;//year-4�� �����ϼ� �����Ƿ� year+56�� ���ش�.// F9�� 9-5=4
	int index1=(cycle%12);
	int index2=(cycle%10);
	printf("%c%c",c[index1],b[index2]);
	return 0;
}