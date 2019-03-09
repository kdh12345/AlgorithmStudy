#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main(void){
	int n,l;
	scanf("%d %d",&n,&l);
	int map[201][101];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			scanf("%d",&map[i][j]);
		}
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			map[i+n][j]=map[j][i];//세로행렬을 가로옆에 붙이기
		}
	}
	bool height_check=true;
	int cnt=0;
	for(int i=0;i<2*n;i++){
		for(int j=1;j<n;j++){
			if(map[i][0]!=map[i][j])
				height_check=false;
		}
		if(height_check)
			cnt++;
	}//가로세로
	bool slide_check=true;
	int i,j=0;
	int h=1;
	for(i=0;i<2*n;i++){
		h=1;
		for(j=0;j<n-1;j++){
			if(map[i][j]==map[i][j+1]){
				h++;
			}
			else if(map[i][j]-1==map[i][j+1]&&h>=1)
			{
				slide_check=true;
				h=1;
			}	
			else if(map[i][j]+1==map[i][j+1]&&h>=1)
			{
				slide_check=true;
				h=1-l;
			}	
			else{
				slide_check=false;
			}
				
		}
		if(j==n-1&&slide_check&&h>=l){
			cnt++;
		}
	}
	
	printf("%d\n",cnt);
	return 0;
}