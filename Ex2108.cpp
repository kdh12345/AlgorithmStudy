#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	int n;
	cin>>n;
	vector<int> v;
	for(int i=0;i<n;i++){
		int num;
		cin>>num;
		v.push_back(num);
	}
	int sum=0;
	for(int i=0;i<n;i++){
		sum+=v[i];
	}
	double avg=(double)sum/n;//출력할때 floor(avg+0.5)
	sort(v.begin(),v.end());
	int num=0;
	num=v[v.size()/2];
	//////////최빈값->
	int cnt=0;
	vector<int> arr;
	int index=0;
	for(int i=0;i<v.size()-1;i++){
		int tmp=v[i];
		int idx=i+1;
		if(tmp==v[idx])
			cnt++;
		else{
			arr[index]=cnt;
			cnt=0;
			index++;
		}
	}//최빈값 세는 함수==>구현 difficult
	sort(arr.begin(),arr.end());
	for(int i=0;i<index;i++){
		if(arr[i]==arr[i+1])

	}
	int result=v.end()-v.begin();
	return 0;
}