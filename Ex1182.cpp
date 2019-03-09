#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#pragma warning(disable:4996)
using namespace std;

int SubSet(vector<int> v,int sum){
	int idx=1;
	int start=0;
	int total=0;//ÇÕ°è!!
	int cnt=0;//°¹¼ö!!
	for(int i=start;i<idx&&idx<=v.size();i++){
		total+=v.at(i);
		if(total==sum)
			cnt++;
		if(idx==v.size())
			idx=start+1;
		if(i==v.size()-1)
		{
			start++;
		}
		if(idx!=v.size())
			idx++;
	}
	return cnt;
}
int main(void){
	vector<int> n;
	int num;
	int sum;
	scanf("%d %d",&num,&sum);
	for(int i=0;i<num;i++){
		int d;
		scanf("%d",&d);
		n.push_back(d);
	}
	int count= SubSet(n,sum);
	printf("%d\n",count);
	return 0;
}