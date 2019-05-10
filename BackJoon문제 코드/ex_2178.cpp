#include <iostream>
#include <queue>
#include <cstring>
using namespace std;
int n, m;
int miro[101][101];
int dx[] = { -1,0,1,0,};
int dy[] = { 0,1,0,-1 };
queue<pair<int,int>> q;
int cnt = -1;
void bfs() {
	int  nextX, nextY;
	q.push({ 0,0 });//출발점이 정해져있음!!
	pair<int, int > now;
	while (!q.empty()) {
		now = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			nextX = now.first + dx[i];
			nextY = now.second + dy[i];
			if (0 <= nextX && nextX < n && 0 <= nextY && nextY < m) {
				if (miro[nextX][nextY] == 1) {
					q.push({ nextX,nextY });
					miro[nextX][nextY] = miro[now.first][now.second]+1;
				}
			}

		}
	}
}
int main(void) {
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf_s("%1d", &miro[i][j]);
		}
	}
	bfs();
	cout << miro[n-1][m-1] << '\n';
	return 0;
}