#include <iostream>
#include <vector>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin>>t;
	int x,y;
	int k=1;
	int cnt=1;
	vector<int> v;
	for(int i=0;i<t;i++){
		cin>>x>>y;
		while(y>x){
			y=y-k;
			if((y-x)>=k+1){
				k=k+1;
				cnt++;
				y=y-x-k;
			}else if((y-x)<k+1){
				cnt++;
				y=y-k;	
			}
		}//y>x
		v.push_back(cnt);
	}
	for(int i=0;i<v.size();i++){
		cout<<v[i]<<"\n";
	}
	return 0;
}