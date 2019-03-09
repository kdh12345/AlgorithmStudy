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
	int cycle=(year)%60;//year-4는 음수일수 있으므로 year+56을 해준다.// F9는 9-5=4
	int index1=(cycle%12);
	int index2=(cycle%10);
	printf("%c%c",c[index1],b[index2]);
	return 0;
}