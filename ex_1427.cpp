#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	string s;
	cin>>s;
	vector<int> v;
	for(int i=0;i<s.length();i++)
	{
		int value=s[i]-'0';
		v.push_back(value);
	}
	sort(v.begin(),v.end(),greater<int>() );
	for(int i=0;i<v.size();i++)
		cout<<v[i];
	return 0;
}