#include <iostream>

using namespace std;



int main() {

	long long number;

	cin >> number;



	long long a, b, c;

	a = 0;

	b = 1;

	c = 1;



	for (long long i = 1; i < (number%1500000); i++) {

		c = a + b;

		a = b % 1000000;

		b = c % 1000000;

	}



	cout << c % 1000000 << endl;

	return 0;

}
