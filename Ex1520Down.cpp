#include <iostream>
using namespace std;
int count=0;
int m,n;
int map[501][501];
bool visit[501][501]={false,};
void road(int x,int y){
	if(x==m-1&&y==n-1){
		count++;
	}
	visit[x][y]=true;
	//위
	if(x>=1&&x<m){
		if(visit[x-1][y]==false&&map[x][y]>map[x-1][y]){
			visit[x-1][y]=true;
			road(x-1,y);
		}
	}
	//아래
	if(x>=0&&x<m){
		if(visit[x+1][y]==false&&map[x][y]>map[x+1][y]){
			visit[x+1][y]=true;
			road(x+1,y);
		}
	}
	//왼쪽
	if(y>=1&&y<n){
		if(visit[x][y-1]==false&&map[x][y-1]<map[x][y]){
			visit[x][y-1]=true;
			road(x,y-1);
		}
	}
	//오른쪽
	if(y>=0&&y<n){
		if(visit[x][y+1]==false&&map[x][y]>map[x][y+1]){
			visit[x][y+1]=true;
			road(x,y+1);
		}
	}
	visit[x][y]=false;
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int m,n;
	cin>>m;
	cin>>n;
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			cin>>map[i][j];
		}
	}
	road(0,0);
	cout<<count<<"\n";
	return 0;
}