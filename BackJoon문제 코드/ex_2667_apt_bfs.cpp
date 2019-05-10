#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;


int N;
int graph[26][26];
int visited[26][26]; 

int dy[] = { -1, 1, 0, 0 }; 
int dx[] = { 0, 0, 1, -1 };

int cnt = 0; //연결 요소(component)의 수
queue<pair<int, int>> q;
vector<int> house_num;

void bfs()
{
	while (!q.empty()) {
		int nowX = q.front().first;
		int nowY = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++)
		{

			int nextX = nowX + dx[i];
			int nextY = nowY + dy[i];

			if (0 <= nextX && nextX < N && 0 <= nextY && nextY < N)
				if (graph[nextX][nextY] == 1 && !visited[nextX][nextY])
				{
					visited[nextX][nextY] = 1;
					cnt++;
					q.push(make_pair(nextX,nextY));
				}
		}
		
	}
	
}

int main(void)
{
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf_s("%1d", &graph[i][j]);
			if (graph[i][j] == 1) {
				q.push(make_pair(i,j));
			}
		}
	}
	bfs();
	sort(house_num.begin(), house_num.end());
	cout << house_num.size() << "\n";
	
	return 0;
}