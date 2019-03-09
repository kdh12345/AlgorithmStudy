#include <cstdio>
#include <iostream>
using namespace std;

int main(void)
{
	int x,y,w,h;
	scanf("%d %d %d %d",&x,&y,&w,&h);
	int result[4]={w-x,x,h-y,y};
	int min=result[3];
	for(int i=0;i<4;i++){
		if(min>result[i])
			min=result[i];
	}
	printf("%d\n",min);
	return 0;
}