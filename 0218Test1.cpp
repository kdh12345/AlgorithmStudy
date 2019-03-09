#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int k;
vector<string> st;
int ans;
bool check[26];///알파벳 검증(문자열이 알파벳으로 이루어져있는지 검증)
void go(int cnt,int start){
	if(cnt==k){
		int cnt_max=0;
		for(int i=0;i<st.size();i++){
			bool c=true;
			for(int j=0;j<st[i].size();j++){
				if(!check[st[i][j]-'a']){
					c=false;
					break;
				}//알파벳 검증		
			}//j
			if(c){
				cnt_max++;
			}
		}
		ans=max(ans,cnt_max);
		return;
	}
	for(int i=start;i<26;i++){
		if(check[i]==false){
			check[i]=true;	
			go(cnt+1,i+1);
			check[i]=false;//check 원래데로 되돌려 다음꺼 검증
		}

	}

}
int main(void){
	cin.tie(0);
	cout.tie(0);
	//int n,k;
	scanf("%d %d",&n,&k);
	//vector<string> st;
	for(int i=0;i<n;i++){
		string str;
		cin>>str;
		st.push_back(str);
		//str.clear();	
	}
	check['a'-'a']=true;
	check['n'-'a']=true;
	check['t'-'a']=true;
	check['i'-'a']=true;
	check['c'-'a']=true;
	k-=5;
	if(k<0){
		cout<<0<<"\n";
		return 0;
	}
	else {
		go(0,0);
		cout<<ans<<"\n";
	
	}
	/*int count=0;
	int wcnt=0;
	bool check=true;
	vector<int> wordCnt;
	for(int p=0;p<n;p++){
	for(int i=4;i<st.at(i).size()-4;i++){
	if(st.at(i)[i]=='a'){
	continue;
	}if(st.at(i)[i]=='n'){
	continue;
	}if(st.at(i)[i]=='t'){
	continue;
	}if(st.at(i)[i]=='i'){
	continue;
	}if(st.at(i)[i]=='c'){
	continue;
	}else{
	count++;
	if(count>k-5)
	check=false;
	else{
	wcnt++;
	check=true;
	}
	}
	}///i
	if(check)
	wordCnt.push_back(wcnt);
	}*/
	return 0;
}