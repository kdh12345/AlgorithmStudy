#include <cstdio>
#include <iostream>
using namespace std;

int sol_one(int num){
	int count=0;
	if(num<=99){
		for(int i=1;i<=num;i++){
			count++;
		}
	}else if(num>99){
		for(int i=1;i<=99;i++){
			count++;
		}
		for(int i=100;i<=num;i++){
			int x=i/100;
			int y=(i%100)/10;
			int z=(i%100)%10;
			if(y-x==z-y)
				count++;
		}
	}
	return count;
}
int main(void){
	int n;
	scanf("%d",&n);
	int cnt=sol_one(n);
	printf("%d\n",cnt);
	return 0;
}