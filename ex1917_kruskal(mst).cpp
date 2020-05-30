#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int parent[10001];
//kruskal(MST를 구하는 방법 1)
struct Edge {
	int u, v, w;
	Edge(int u, int v, int w) {
		this->u = u;
		this->v = v;
		this->w = w;
	}
};
bool cmp(Edge a, Edge b) {
	return a.w < b.w;//오름차순
}
int find(int u) {
	if (u == parent[u])
		return u;
	else
		return parent[u] = find(parent[u]);
}
void merge(int u, int v) {
	u = find(u);
	v = find(v);
	parent[v] = u;
}
int main(void) {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int v, e;
	cin >> v >> e;
	vector<Edge> V;
	auto ans = 0;
	int a, b, c;
	for (int i = 1; i <= v; i++)
		parent[i] = i;
	for (int i = 0; i < e; i++) {
		cin >> a >> b >> c;
		V.push_back(Edge(a, b, c));
	}
	sort(V.begin(), V.end(),cmp);
	for (auto n : V) {
		if (find(n.v) != find(n.u)) {
			merge(n.u, n.v);
			ans += n.w;
		}
	}
	cout << ans << '\n';
	return 0;
}