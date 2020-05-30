#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAX = 987654321;
int dist[20001];
vector<pair<int, int> > arr[20001];
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int v, e;
	cin >> v >> e;
	int start;
	cin >> start;
	
	for (int i = 0; i < e; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		arr[u].push_back(make_pair(v, w));
	}//간선 + 가중치 저장
	fill(dist, dist + v + 1, MAX);//최소값구하는 방법1
	dist[start] = 0;//시작정점 표시
	priority_queue<pair<int, int> > pq;
	pq.push(make_pair(0, start));
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int here = pq.top().second;
		pq.pop();
		for (int i = 0; i < arr[here].size(); i++) {
			int next = arr[here][i].first;
			int nextCost = arr[here][i].second;
			if (dist[next] > dist[here] + nextCost) {
				dist[next] = dist[here] + nextCost;
				pq.push(make_pair(-dist[next], next));
			}
		}
	}
	for (int i = 1; i <= v; i++) {
		if (dist[i] == MAX) {
			cout << "INF" << '\n';
			continue;
		}
		cout << dist[i] << '\n';
	}
	return 0;
}