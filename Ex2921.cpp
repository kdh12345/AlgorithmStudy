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
	}//N�� 1�̸� 1 N�� 2�̸� 1����2 N��3 1����3 N�� 4�̸�
	//1~4
	printf("%d\n",total);
	return 0;

}