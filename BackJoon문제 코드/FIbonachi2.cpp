#include <stdio.h>
//n은 자연수 이므로 
long long Fibo(int n){
	long long a=0;
	long long b=1;
	long long tmp;
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