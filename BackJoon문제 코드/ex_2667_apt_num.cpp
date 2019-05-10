#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int N;
int graph[26][26];
int visited[26][26]; //방문했다고 표시

int dy[] = { -1, 1, 0, 0 }; // 남, 북, 동, 서
int dx[] = { 0, 0, 1, -1 };

int cnt = 0; //연결 요소(component)의 수

void DFS(int x, int y)
{
	for (int i = 0; i < 4; i++)
	{
		
		int nextX = x + dx[i];
		int nextY = y + dy[i];

		if (0 <= nextX && nextX < N && 0 <= nextY && nextY < N)
			if (graph[nextX][nextY]==1 && !visited[nextX][nextY])
			{
				visited[nextX][nextY] = 1;
				cnt++;
				DFS(nextX, nextY);
			}
	}
}

int main(void)
{
	cin.tie(0);
	cout.tie(0);
	cin >> N;

	

	vector<int> houseNum;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			scanf_s("%1d", &graph[i][j]);
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (graph[i][j]==1 && !visited[i][j])
			{
				visited[i][j] = 1;
				cnt++;
				DFS(i, j);
				houseNum.push_back(cnt);
				cnt = 0; 
			}
		}
		
	}
	sort(houseNum.begin(), houseNum.end());

	cout << houseNum.size() << "\n";

	for (int i = 0; i < houseNum.size(); i++) {
		cout << houseNum[i] << "\n";
	}

	return 0;
}