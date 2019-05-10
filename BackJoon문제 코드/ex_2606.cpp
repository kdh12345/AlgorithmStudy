#include <iostream>
using namespace std;
int adj[101][101];
int visit[101];
int n, m;//n->컴퓨터수 
//m->network상에서 직접 연결되어있는 컴퓨터 쌍의 수가 주어진다.
int cnt = -1;
void dfs(int index) {
	for (int i = 1; i <= n; i++) {
		if (!visit[i] && adj[index][i]) {
			visit[i] = 1;
			dfs(i);
			cnt++;
		}
	}
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int from, to;
		cin >> from >> to;
		adj[from][to] = 1;
		adj[to][from] = 1;//상호연결
	}
	visit[0] = 1;
	dfs(1);
	cout << cnt << '\n';
	return 0;
}