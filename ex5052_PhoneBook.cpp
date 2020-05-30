#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		vector<string> v;
		for (int j = 0; j < n; j++) {
			string phone;
			cin >> phone;	
			v.push_back(phone);
		}
		sort(v.begin(), v.end());
		bool flag = false;
		for (int j = 1; j < v.size(); j++) {
			string cmp = v[j].substr(0, v[j - 1].length());//현재vs이전
			if (cmp == v[j - 1]) {
				flag = true;
				break;
			}
		}
		if (flag) {
			cout << "NO" << '\n';
		}
		else {
			cout << "YES" << '\n';
		}

	}
	return 0;
}