#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int direction[4]={1,-1,-1,1};
vector<int> xt;
vector<int> yt;
void DragonCurve(int x,int y,int d,int g){
	if(d==0){

		x+=direction[0];
	}

}
int main(void){
	cout.tie(0);
	cin.tie(0);
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		string input;
		cin>>input;
		int x=input[0];
		int y=input[1];
		int d=input[2];
		int g=input[3];
		DragonCurve(x,y,d,g);
	}
	

	return 0;
}