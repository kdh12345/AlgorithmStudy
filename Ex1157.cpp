#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
	string str;
	string ans="";
	vector<char> result;
	cin>>str;
	for(int i=0;str.size();i++){
		str[i]=toupper(str[i]);
	}
	int arr[26];//26개의 알파벳
	for(int i=0;i<str.size();i++){
		result.push_back(str[i]);
	}
	for(int i=0;i<str.size();i++){
		arr[result.at(i)-'A']++;//문자는 문자끼리계산해서 ascii코드이용
	}
	int max=arr[0];
	int len=sizeof(arr)/sizeof(int);
	for(int i=0;i<len;i++){
		if(max<arr[i])
		{	
			max=arr[i];
			ans[i]=((char)(65+i));
		}
		else if(max==arr[i])///max가 여러개
			ans[i]='?';
	}
	printf("%s",ans);
	printf("\n");
	return 0;

}