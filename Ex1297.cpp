#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	int w_rate;int h_rate;double diagonal;
	scanf("%lf %d %d",&diagonal,&w_rate,&h_rate);
	double pre=w_rate*w_rate+h_rate*h_rate;
	double result=(diagonal*diagonal)/pre;
	double k=sqrt(result);
	int width=floor(k*w_rate);
	int height=floor(k*h_rate);
	printf("%d %d\n",width,height);
	return 0;
}