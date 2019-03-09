#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#pragma warning(disable:4996)
using namespace std;
int n;
int operators[4];
vector<int> str;//수 입력
int Max;
int Min;
void Sol(int index,int result);


int main(void)
{
	scanf("%d",&n);
	int num=0;
	for(int i=0;i<n;i++){
		scanf("%d",&num);
		str.push_back(num);
	}
	for(int i=0;i<4;i++){
		scanf("%d",&operators[i]);
	}
	Max=str.at(0);
	Min=str.at(str.size()-1);
	Sol(1,str.at(0));
	printf("%d\n",Max);
	printf("%d\n",Min);
	return 0;
}
void Sol(int index,int result){
	if(index>=n)
	{
		Max=max(Max,result);
		Min=min(Min,result);
		return;
	}
	int len=sizeof(operators)/sizeof(int);
	for(int i=0;i<len;i++){
		if(operators[i]==0) //연산자가 없을때!!!
			continue;
		operators[i]--;
		switch(i){
		case 0:
			Sol(index+1,result+str.at(index));
			break;
		case 1:
			Sol(index+1,result-str.at(index));
			break;
		case 2:
			Sol(index+1,result*str.at(index));
			break;
		case 3:
			Sol(index+1,result/str.at(index));
			break;
		}
	}
}


