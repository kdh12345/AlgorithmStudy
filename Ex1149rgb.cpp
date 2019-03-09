#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int main(void){
	cin.tie(0);
	cout.tie(0);
	int n;
	int rgb[1001][3]={0,};

	cin>>n;
	for(int i=1;i<=n;i++){
		for(int j=0;j<3;j++){
			cin>>rgb[i][j];
		}
	}
	for(int i=1;i<=n;i++){
		rgb[i][0]+=min(rgb[i-1][1],rgb[i-1][2]);
		rgb[i][1]+=min(rgb[i-1][0],rgb[i-1][2]);
		rgb[i][2]+=min(rgb[i-1][0],rgb[i-1][1]);
	}
	cout<<min(min(rgb[n][0],rgb[n][1]),rgb[n][2])<<"\n";
	return 0;
}