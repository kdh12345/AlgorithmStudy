#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	string a, b;
	cin >> a >> b;
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	string new_str = "";
	string long_s;
	string short_s;
	if (a.length() >= b.length()) {
		long_s = a;
		short_s = b;
	}
	else {
		long_s = b;
		short_s = a;
	}
	int diff = long_s.length() - short_s.length();
	int carry = 0;
	for (int i = 0; i < diff; i++) {
		short_s += "0";
	}
	for (int i = 0; i < long_s.size(); i++) {
		int sum = stoi(long_s.substr(i, 1)) + stoi(short_s.substr(i, 1)) + carry;
		if (sum >= 10) {
			carry = 1;
			sum %= 10;
		}
		else
			carry = 0;
		new_str += to_string(sum);
	}
	if (carry != 0)
		new_str += to_string(carry);
	reverse(new_str.begin(), new_str.end());
	cout << new_str << '\n';
	return 0;
}