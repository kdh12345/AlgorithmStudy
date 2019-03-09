
#include <iostream>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

bool reve;
bool error;
void RD(string cmd,deque<int> dq){
	cout.tie(0);
	for(int i=0;i<cmd.size();i++){
		if(cmd[i]=='R'){
			reve=!reve;
		}else if(cmd[i]=='D'){
			if(dq.empty()){
				error=true;
				break;
			}
			if(reve)dq.pop_back();
			else
				dq.pop_front();
		}
	}//cmd
	if(!error){
		cout<<"[";
		if(reve)reverse(dq.begin(),dq.end());
		for(int i=0;i<dq.size();i++){
			printf("%d",dq[i]);
			if(i<dq.size()-1)cout<<",";
		}
		cout<<"]"<<"\n";
	}else if(error){
		cout<<"error"<<"\n";
	}
}
int main(void){
	cin.tie(0);
	int t;
	cin>>t;


	for(int i=0;i<t;i++){
		error=false;
		reve=false;
		deque<int> dq;
		string command="";//테스트케이스마다 초기화
		string num="";
		string input="";
		cin>>command;//ex)RDD
		cin>>num;
		cin>>input;
		int x=0;
		for(int i=0;i<input.size();i++){
			if(input[i]>='0'&&input[i]<='9')
				x=x*10+input[i]-'0';
			else{
				if(x>0)
					dq.push_back(x);
				x=0;
				if(input[i]==']')
					break;
			}
		}
		RD(command,dq);
	}//i
	return 0;
}