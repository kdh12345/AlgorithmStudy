#include <iostream>
#include <deque>
using namespace std;
deque<int> dq;
int get_index(int n) {
	int index = 0;
	for (int i = 0; i < dq.size(); i++) {
		if (dq[i] == n) {
			index = i;
		}
	}
	return index;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n, m;
	cin >> n >> m;
	int arr[51];
	for (int i = 0; i < m; i++)
		cin >> arr[i];
	int idx = 0;
	int cnt = 0;
	int count = 0;
	for (int i = 0; i < n; i++)
		dq.push_back(i + 1);
	for(int i=0;i<m;i++) {
		int mid = (dq.size()-1) / 2;
		count = 0;
		if (get_index(arr[idx])<= mid) {
			int now = arr[idx];
			while (now!=dq.front()) {
				int pre = dq.front();
				dq.pop_front();
				dq.push_back(pre);
				count++;
				
			}
			if (now == dq.front())
			{
				dq.pop_front();
			}
		}
		else {
			int now = arr[idx];
			while (now!=dq.front()) {
				int pre = dq.back();
				dq.pop_back();
				dq.push_front(pre);
				count++;
			}
			if (now == dq.front())
			{
				dq.pop_front();
			}
		}
		idx++;
		cnt += count;
	}
	cout << cnt << '\n';
	return 0;
}