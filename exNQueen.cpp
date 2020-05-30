#include <iostream>
using namespace std;


bool visit[15][15] = { false, };
int cnt;
int n;
bool check(int row, int col) {
	for (int i = 0; i < n; i++) {
	
		if (visit[i][col])
			return false;
	}
	int x = row - 1;
	int y = col + 1;
	while (x >= 0 && y < n) {
		if (visit[x][y])
			return false;
		x--;
		y++;
	}
	x = row - 1;
	y = col - 1;
	while (x >= 0 && y >= 0) {
		if (visit[x][y])
			return false;
		x--;
		y--;
	}
	return true;
}
void dfs(int row) {
	if (row == n) {
		cnt++;
		return;
	}
	for (int i = 0; i < n; i++) {
		if (check(row, i)) {
			visit[row][i] = true;
			dfs(row + 1);
			visit[row][i] = false;
		}
		
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n;
	dfs(0);
	cout << cnt << '\n';
	return 0;
}