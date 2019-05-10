#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int test_case;
	cin >> test_case;
	deque<int> dq;
	while (test_case > 0) {
		string s;
		cin >> s;
		if (s == "push_back") {
			int value;
			cin >> value;
			dq.push_back(value);
		}
		else if (s.substr(0, 10) == "push_front") {
			int value;
			cin >> value;
			dq.push_front(value);
		}
		else if (s == "front") {
			if (dq.empty()) {
				cout << -1 << '\n';
			}
			else
				cout << dq.front() << '\n';
		}
		else if (s == "back") {
			if (dq.empty()) {
				cout << -1 << '\n';
			}
			else
				cout << dq.back() << '\n';
		}
		else if (s == "size") {
			cout << dq.size() << '\n';
		}
		else if (s == "empty") {
			if (dq.empty()) {
				cout << 1 << '\n';
			}
			else
				cout << 0 << '\n';
		}
		else if (s == "pop_front") {
			if (dq.empty()) {
				cout << -1 << '\n';
			}
			else {
				int num = dq.front();
				dq.pop_front();
				cout << num << '\n';
			}
		}
		else if (s == "pop_back") {
			if (dq.empty()) {
				cout << -1 << '\n';
			}
			else {
				int num = dq.back();
				dq.pop_back();
				cout << num << '\n';
			}
		}
		test_case--;
	}
}