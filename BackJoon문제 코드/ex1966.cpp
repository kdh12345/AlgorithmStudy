#include<iostream>
#include <queue>
using namespace std;

int printer_q(int n, int m, queue<pair<int, int>> q, priority_queue<int> pq) {
	int cnt = 0;
	if (n == 1) {
		cnt++;
		return cnt;
	}
	while (!q.empty()) {
		int idx = q.front().first;
		int value = q.front().second;
		q.pop();
		if (pq.top() == value) {
			cnt++;
			pq.pop();
			if (idx == m) {
				break;
			}
		}
		else {
			q.push({ idx, value });
		}
	}
	return cnt;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int test_case;
	cin >> test_case;
	for (int i = 0; i < test_case; i++) {
		int n, m;
		cin >> n >> m;
		queue<pair<int, int>> q;
		priority_queue<int> pq;
		for (int j = 0; j < n; j++) {
			int num;
			cin >> num;
			q.push({ j,num });
			pq.push(num);
		}
		cout << printer_q(n, m, q, pq) << '\n';
	}
	return 0;
}