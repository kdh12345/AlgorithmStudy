#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

const int MAX = 1000 + 1;

int n, m, v;

int adj[MAX][MAX];
bool visit[MAX];
queue<int> q;

void dfs(int index) {
	cout << index << ' ';
	for (int i = 1; i <= n; i++) {
		if (adj[index][i] && !visit[i]) {
			visit[i] = true;
			//������ ���� �ٽ� dfs stack->recursive call->function call
			dfs(i);
		}
	}
}
void bfs(int index) {
	q.push(index);
	visit[index] = true;
	while (!q.empty()) {
		index = q.front();
		q.pop();
		cout << index << ' ';
		//bfs�� �ش� ����� ���� ������ ��� �߰��ѵ� bfs����
		for (int i = 1; i <= n; i++){
			if (adj[index][i] && !visit[i]) {
				visit[i] = 1;
				q.push(i);
			}
		}
			
	}
}

int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n >> m >> v;
	for (int i = 0; i < m; i++) {
		int from, to;
		cin >> from >> to;
		adj[from][to] = 1;
		adj[to][from] = 1;//��ȣ����
	}
	visit[v] = 1;
	dfs(v);
	cout << '\n';
	memset(visit, false, sizeof(visit));
	bfs(v);
	cout << '\n';
	return 0;

}