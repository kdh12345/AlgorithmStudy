#include <cstdio>
#include <iostream>
using namespace std;
int place[10000][51];
int n,m;//ũ��
int r,c,d;
int count=1;
bool visit[50][50]={false,};
int pre=d;
void Cleaning(int r,int c){
	if(visit[r-1][c]==true&&visit[r][c-1]==true&&visit[r+1][c]==true&&visit[r][c+1]==true){
		if(d==0){//����
			Cleaning(r,--c);
		}else if(d==1){//����
			Cleaning(--r,c);
		}else if(d==2){//����
			Cleaning(r,++c);
		}else if(d==3){
			Cleaning(++r,c);
		}
	}
	if(place[r-1][c]==1&&place[r][c-1]==1&&place[r+1][c]==1&&place[r][c+1]==1){
		printf("%d\n",count);
		return;
	}
	if(place[r-1][c]==1){
		printf("%d\n",count);
		return;
	}//place[r-1][c]==1
	else if(place[r-1][c]==0||visit[r-1][c]==false){
		d=3;
		if(r<0){
			printf("%d\n",count);
			return;
		}
		count++;
		Cleaning(--r,c);
	}
	d=pre;

}
int main(void){
	scanf("%d %d",&n,&m);
	scanf("%d %d %d",&r,&c,&d);//��ǥ�� ����
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			scanf("%d",&place[i][j]);//����� ����
		}
	}//for��
	Cleaning(r,c);
	return 0;
}