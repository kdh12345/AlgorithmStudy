#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string chess[51];
///흰 검 기준 배열 2개만들기!!
const char color1[9][9]={
		{"WBWBWBWB"},
		{"BWBWBWBW"},
		{"WBWBWBWB"},
		{"BWBWBWBW"},
		{"WBWBWBWB"},
		{"BWBWBWBW"},
		{"WBWBWBWB"},
		{"BWBWBWBW"}
	};
const char color2[9][9]={
		{"BWBWBWBW"},
		{"WBWBWBWB"},
		{"BWBWBWBW"},
		{"WBWBWBWB"},
		{"BWBWBWBW"},
		{"WBWBWBWB"},
		{"BWBWBWBW"},
		{"WBWBWBWB"}
	};
int White(int x,int y){
	int count=0;
	for(int i=x;i<x+8;i++){
		for(int j=y;j<y+8;j++){
			if(chess[i][j]!=color1[i-x][j-y])
				count++;
		}
	}
	return count;
	
}
int Black(int x,int y){//x와 y는 기준점
	int count=0;
	for(int i=x;i<x+8;i++){
		for(int j=y;j<y+8;j++){
			if(chess[i][j]!=color2[i-x][j-y])
				count++;
		}
	}
	return count;
	
	
}
int main(void)
{
	int m,n;
	scanf("%d %d",&m,&n);
	int count=0;
	string str="";
	for(int i=0;i<m;i++){
		cin>>str;
		chess[i]=str;
	}
	int cnt=12345678;
	for(int i=0;i+7<m;i++){
		for(int j=0;j+7<n;j++){
			cnt=min(cnt,min(Black(i,j),White(i,j)));
		}
	}
	printf("%d\n",cnt);
	return 0;

}