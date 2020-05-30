#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int INF = 987654321;
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n, m;
	cin >> n >> m;
	vector<pair<int, int> > arr[1001];
	for (int i = 0; i < m; i++) {
		int from, to, cost;
		cin >> from >> to >> cost;
		arr[from].push_back(make_pair(to, cost));
	}
	int start, end;
	cin >> start >> end;
	int dist[1001];
	fill(dist, dist + n + 1, INF);
	priority_queue<pair<int, int> > pq;

	pq.push(make_pair(0, start));
	dist[start] = 0;
	while (!pq.empty()) {
		int c = -pq.top().first;
		int visit = pq.top().second;
		pq.pop();
		for (int i = 0; i < arr[visit].size(); i++) {
			int next = arr[visit][i].first;
			int nextCost = arr[visit][i].second;

			if (dist[next] > dist[visit] + nextCost) {
				dist[next] = dist[visit] + nextCost;
				pq.push(make_pair(-dist[next], next));
			}
		}
	}
	int total = dist[end];
	cout << total << '\n';
	return 0;
}