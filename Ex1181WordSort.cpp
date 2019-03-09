#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
#pragma warning(disable:4996)
bool comp(const string &s1,const string &s2){
	if(s1.size()==s2.size()){
		return s1<s2;//사전순정렬(기본)
	}else
		return s1.size()<s2.size();//길이순정렬
}//기억!!!!
int main(void)
{
	cin.tie(0);
	cout.tie(0);
	int len;
	cin>>len;
	vector<string> v;
	for(int i=0;i<len;i++){
		string str;
		cin>>str;
		v.push_back(str);
		str.clear();
	}
	sort(v.begin(),v.end(),comp);
	v.erase(unique(v.begin(),v.end()),v.end());
	for(int i=0;i<v.size();i++){
		cout<<v[i]<<"\n";
	}
	
	return 0;
}