#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <cstdlib>
using namespace std;
char str[21];
map<string,int> name;
string pokemon_num[100001];
int n,m;
int main(void){
	cin.tie(0);
	cout.tie(0);
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++){
		cin>>str;
		string s=str;
		name.insert(make_pair(s,i+1));
		pokemon_num[i]=s;
	}
	for(int i=0;i<m;i++){
		cin>>str;
		if(isdigit(str[0])){
			cout<<pokemon_num[atoi(str)-1]<<"\n";
		}else{
			string st=str;
			cout<<name[st]<<"\n";
		}
	}
	return 0;
}
