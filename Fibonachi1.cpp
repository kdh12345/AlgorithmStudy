#include <stdio.h>

int Fibo(int n){
	int a=0;
	int b=1;
	int tmp;
	for(int i=0;i<n-1;i++){
		tmp=b;
		b=a+b;
		a=tmp;
	}
	return b;
	
}
int main(void){
	int n;
	scanf("%d",&n);
	long long result=Fibo(n);
	printf("%lld\n",result);
	return 0;

}