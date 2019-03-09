#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main(void)
{
	int T;
	scanf("%d",&T);
	int R;
	string str;
	string ans;
	for(int i=0;i<T;i++){
		scanf("%d",&R);
		cin>>str;
		int len=str.length();
		for(int j=0;j<len;j++){
			ans+=str[j];
		}
		printf("%s",ans);
		printf("\n");
	}
	
	return 0;
}