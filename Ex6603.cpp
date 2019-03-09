#include <iostream>
#include <cstdio>
using namespace std;
#define max 13
int lotto_num[max];
int ans[max];
//vector<int> lotto_num;
//vecotr<int> ans;
int k;

void dfs(int start,int level){
	cout.tie(0);
	if(level==6){
		for(int i=0;i<6;i++){
			cout<<ans[i]<<" ";
			//cout<<ans.at(i)<<" ";
		}
		cout<<"\n";
		return;
	}
	for(int i=start;i<k;i++){//start~k-1까지 탐색
		ans[level]=lotto_num[i];
		//ans.at(level)=lotto_num.at(i);
		dfs(i+1,level+1);
	}

}
int main(void)
{
	cout.tie(0);//속도향상
	cin.tie(0);//속도향상
	while(1){
		cin>>k;
		if(k==0)break;

		for(int i=0;i<k;i++)
			cin>>lotto_num[i];
		//cin>>lotto_num.at(i);

		dfs(0,0);
		cout<<"\n";
	}
	return 0;
}