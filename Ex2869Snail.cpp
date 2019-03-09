#include <iostream>
#include <cstdio>
using namespace std;

int main(void)
{
	int A,B,V;
	scanf("%d",&A);scanf("%d",&B);scanf("%d",&V);
	int num=0; // A A-B A-B+A .... A+num*(A-B)<=V
	if((V-A)%(A-B)){
		num=(V-A)/(A-B)+2;//ex) 3 1 6
	}else // 2 1 5
		num=(V-A)/(A-B)+1;
	printf("%d\n",num);
	return 0;

}