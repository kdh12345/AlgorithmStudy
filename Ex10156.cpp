#include <cstdio>
#include <iostream>
using namespace std;

int main(void)
{
	int k,n,m;
	scanf("%d",&k);scanf("%d",&n);scanf("%d",&m);
	int result=m-k*n;
	int mom=0;
	if(result<=0)
		mom=result*-1;
	printf("%d\n",mom);

}