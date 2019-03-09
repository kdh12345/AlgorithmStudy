#include <cstdio>
#include <iostream>
using namespace std;

int main(void)
{
	int hour;int min;
	scanf("%d %d",&hour,&min);
	int cook;
	scanf("%d",&cook);
	hour+=cook/60;
	min+=cook%60;
	if(min>=60){
		hour++;
		min-=60;
	}
	if(hour>=24){
		hour=hour-24;
	}
	printf("%d %d\n",hour,min);
	return 0;
}