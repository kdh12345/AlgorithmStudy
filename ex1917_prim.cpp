#include <iostream>
#include <vector>
#include <queue>
using namespace std;
//prim(MST구하기)
int visit[10001];
vector<pair<int, int> > edge[10001];

int prim() {
	auto ans = 0;
	priority_queue<pair<int, int> , vector<pair<int, int> >, greater<pair<int, int>  > > pq;
	pq.push(make_pair(0,1));//1번 정점 부터 minheap, 가중치는 0부터

	while (!pq.empty()) {
		pair<int, int> cur = pq.top();
		pq.pop();

		if (visit[cur.second] == 1)
			continue;
		visit[cur.second] = 1;
		ans += cur.first;//가중치 더함
		for (int i = 0; i < edge[cur.second].size(); i++) {
			if (visit[edge[cur.second][i].second] == 0) {//현재 정점에서 방문하지 않은 정점 넣기
				pq.push(edge[cur.second][i]);
			}
		}
	}
	return ans;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int v, e;
	cin >> v >> e;
	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		edge[a].push_back(make_pair(c, b));
		edge[b].push_back(make_pair(c, a));
	}
	auto res = prim();
	cout << res << '\n';
	return 0;
}