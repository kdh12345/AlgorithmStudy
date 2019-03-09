#include <cstdio>
#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <sstream>
using namespace std;

void Sol(string str){
	cout.tie(0);
	/*int idx=0;
	while(str[idx]!=' '){
		idx++;
	}
	int cnt=0;
	deque<char> st;
	for(int i=idx+1;i<str.size();i++){
		if(str[i]==','){
			cnt++;
			i=idx+1;
		}
		if(str[i]=='*'){
			st.push_front(str[i]);
			i++;
		}else if(str[i]=='['){
			st.push_front(str[i]);
			if(str[i+1]==']')
			{
				st.push_front(str[i+1]);
				i++;
			}	
		}else if(str[i]=='&'){
			st.push_front(str[i]);
			i++;
		}
		
	}//for
	vector<string> v;
	for(int i=0;i<cnt;i++){
		for(int j=0;j<idx;j++){
			v.push_back(str[i][j]);
		}
	}*/
	//그냥 출력하자
	for(int i=str.size()-2;i>=0;i--){ //앞에서부터가면 *&[]출력x
		if(str[i]=='&'||str[i]=='*')
			cout<<str[i];
		else if(str[i]==']')
		{
			cout<<"[]";
			i--;
		}
		else{//변수
			cout<<' ';
			for(int j=0;j<=i;j++){
				cout<<str[j];
			}	
			cout<<";\n";//마지막은 항상";"로 끝난다.
			break;
		}
	}


	
}
int main(void){
	string input;
	getline(cin,input);
	stringstream ss;
	ss.str(input);
	string data,var;
	ss>>data;//int&
	while(ss>>var){
		cout<<data;
		Sol(var);
	}
	return 0;
}