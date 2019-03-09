#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(void){
	int N;
	scanf("%d",&N);
	vector<int> weight;
	vector<int> height;
	vector<int> ranking;
	for(int i=0;i<N;i++){
		int w,h;
		scanf("%d %d",&w,&h);
		weight.push_back(w);
		height.push_back(h);
		ranking.push_back(1);
	}
	int rank=1;
	for(int i=0;i<N;i++){
		rank=1;
		for(int j=0;j<N;j++){
			if(weight.at(i)<weight.at(j)&&height.at(i)<height.at(j)){
				ranking.at(i)++;
			}

		}
	}
	for(int i=0;i<ranking.size();i++){
		printf("%d ",ranking.at(i));
	}
	return 0;
}