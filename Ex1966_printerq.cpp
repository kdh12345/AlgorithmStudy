#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int printer_q(int n,int m,vector<int> q){
	int cnt=0;
	if(n==1){
		cnt++;
		return cnt;
	}
	int idx=m;
	int j=1;
	for(int i=0;i<q.size()-1;i++){
		for(j=1;j<q.size();j++){
			if(q[i]<q[j]){
				int pre=q.front();
				q.erase(q.begin());
				q.push_back(pre);
				idx--;
				if(idx<0)
					idx=q.size()-1;
				break;
			}//������ �߿䵵 ū�� ã��
		}
		if(j==q.size()){
			if(idx==0){
				cnt++;
				break;
			}
			q.erase(q.begin());
			cnt++;
		}

	}
	return cnt;
}
int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin>>t;//�׽�Ʈ ���̽�����
	priority_queue<int> q;
	vector<int> v;
	for(int i=0;i<t;i++){
		int n,m;
		cin>>n>>m;
		for(int i=0;i<n;i++){
			int num;//�� ��
			cin>>num;
			v.push_back(num);
			q.push(num);
		}//i
	}//�׽����̽� �ݺ���
	return 0;
}