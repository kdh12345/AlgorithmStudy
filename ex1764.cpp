#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void)
{
		int n;int m;
		vector<string> set;
		vector<string> result;
		vector<string> pre; 
		for(int i=0;i<n;i++) {
			string name;
			scanf("%s",name);
			set.push_back(name);
		}
		int count=0;
		for(int i=0;i<m;i++) {		
			string str;
			scanf("%s",str);
			pre.push_back(str);
			
		}
		for(int i=0;i<m;i++) {
			if(set.pre.at(i))
			{
				result.push_back(pre.at(i));
				count++;
			}
		}
		sort(result.begin(),result.end());
		printf("%d\n",count);
		for(int i=0;i<result.size();i++)
			printf("%d\n",result.at(i));
	}

}