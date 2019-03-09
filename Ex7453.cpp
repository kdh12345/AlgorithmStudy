#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
	int n;
	scanf("%d",&n);
	vector<int> v;
	for(int i=0;i<n*4;i++){
		int num;
		cin>>num;
		v.push_back(num);
	}
	sort(v.begin(),v.end());
	for(int i=0;i<v.size();i++){
		for(int j=0;j<v.size();j++){
			
		}
	}

	return 0;
}