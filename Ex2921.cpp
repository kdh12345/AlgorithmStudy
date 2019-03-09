#include <cstdio>
#include <iostream>
using namespace std;

int main(void)
{
	int n;
	scanf("%d",&n);
	int total=0;
	for(int i=0;i<=n;i++){
		for(int j=0;j<=i;j++){
			total+=j+i;
		}
	}//N이 1이면 1 N이 2이면 1부터2 N이3 1부터3 N이 4이면
	//1~4
	printf("%d\n",total);
	return 0;

}