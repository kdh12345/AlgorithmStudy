#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
int n;
int tri[501][501];
void SolMax(){
	cout.tie(0);
	int d[501][501];
	d[0][0]=tri[0][0];//level=1狼 箭磊
	for(int i=1;i<n;i++){
		for(int j=0;j<=i;j++){
			if(j==0)//力老 哭率
				d[i][j]=d[i-1][j]+tri[i][j];
			else if(j==i)//力老 坷弗率
				d[i][j]=d[i-1][j-1]+tri[i][j];
			else
				d[i][j]=max(d[i-1][j]+tri[i][j],d[i-1][j-1]+tri[i][j]);
		}	
	}
	int m=0;
	for(int i=1;i<n;i++){
		m=max(m,d[n-1][i]);
	}
	cout<<m<<"\n";
	
}
int main(void){
	cin.tie(0);
	cin>>n;
	
	for(int i=0;i<n;i++){
		for(int j=0;j<=i;j++){
			cin>>tri[i][j];
		}
	}
	SolMax();
	return 0;
}
