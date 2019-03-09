#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n;
	cin>>n;
	vector<int> v;
	for(int i=0;i<n;i++){
		int num;
		cin>>num;
		v.push_back(num);
	}
	sort(v.begin(),v.end());
	int cnt=0;
	for(int i=2;i<v[v.size()-1];i++){
		for(int j=0;j<v.size();j++){
			if(v[j]%i==0){
				break;
			}else{
				cnt++;
				break;
			}
				
				
		}
	}
	cout<<cnt<<"\n";
	return 0;
}