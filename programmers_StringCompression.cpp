#include <string>
#include <vector>

using namespace std;

int solution(string s) {
	int answer = s.length();
	if (s.length() == 1) {
		answer = 1;
		return answer;
	}
	int siz = s.length() / 2;
	for (int i = 1; i <= siz; i++) {
		int pos = 0;
		int len = s.length();
		while (true) {
			string word = s.substr(pos, i);//pos~i���� ��ŭ
			pos += i;
			if (pos >= s.length())
				break;
			int cnt = 0;
			while (true) {
				string cmp = s.substr(pos, i);
				if (word == cmp) {
					cnt++;
					pos += i;
				}
				else {
					break;
				}
			}//������ �˻� �ϴ� �˰���
			if (cnt > 0) {
				len -= i * cnt;//���̸� i*cnt��ŭ ���̱� ���� ab->2
				if (cnt < 9) {
					len += 1;
				}
				else if (cnt < 100) {
					len += 2;
				}
				else if (cnt < 1000) {
					len += 3;
				}
				else {
					len += 4;
				}
			}
			if (answer > len)
				answer = len;
		}//�ٱ� while(true)

	}
	return answer;
}