#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void sol_height(vector<int> vec){
	sort(vec.begin(),vec.end());
	int total=0;
	for(int i=0;i<vec.size();i++){
		total+=vec.at(i);
	}
	int idx1=0;
	int idx2=8;
	int pre1=0;int pre2=0;
	for(int i=0;i<vec.size();i++){
		for(int j=i+1;j<vec.size();j++){
			if(total-(vec.at(i)+vec.at(j))==100)
			{
				pre1=i;
				pre2=j;
			
			}
		}
	}
	vector<int> result;
	for(int i=0;i<vec.size();i++){
		if(i==pre1||i==pre2)
			continue;
		else
			result.push_back(vec.at(i));
	}
	for(int i=0;i<result.size();i++){
		printf("%d\n",result.at(i));
	}

}
int main(void){
	vector<int> n;
	for(int i=0;i<9;i++){
		int num;
		scanf("%d",&num);
		n.push_back(num);
	}
	sol_height(n);
	return 0;
}