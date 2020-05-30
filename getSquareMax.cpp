#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
//dp 2차원 배열을 탐색하면서 최댓값 혹은 최솟값 구하기
int solution(vector<vector<int>> board)
{
	int answer = 0;
	int lenX = board.size();
	int lenY = board[0].size();
	if (lenX == 1 || lenY == 1) {
		for (int i = 0; i < lenX; i++) {
			for (int j = 0; j < lenY; j++) {
				if (board[i][j] == 1) {
					answer = 1;
				}
			}
		}
	}
	else {
		for (int i = 1; i < board.size(); i++) {
			for (int j = 1; j < board[i].size(); j++) {
				if (board[i][j] == 1) {
					board[i][j] = min(board[i - 1][j - 1], min(board[i][j - 1], board[i - 1][j])) + 1;
					if (answer < board[i][j]) {
						answer = board[i][j];
					}
				}
			}
		}
		answer *= answer;
	}
	return answer;
}