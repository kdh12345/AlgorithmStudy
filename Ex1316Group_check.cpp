#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

bool WordCheck(string str){
	bool alphabet[26]={false};

	for(int i=0;i<str.length();i++){
		if(alphabet[str[i]-'a']){//이미 있는 알파벳
			return false;
		}else{
			char tmp=str[i];
			alphabet[str[i]-'a']=true;
			while(1){
				if(tmp!=str[++i]){//다른 알파벳 만나면 빠져나옴
					i--;
					break;
				}
			}
		}

	}

	return true;
}

int main(void){
	int n;
	scanf("%d",&n);
	int cnt=0;
	for(int i=0;i<n;i++){
		string s;
		cin >> s;
		if(WordCheck(s)){
			cnt++;
		}
	}
	printf("%d\n",cnt);
	return 0;
}