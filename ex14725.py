import sys


class Trie:
    def __init__(self):
        self.root=dict()

    def add(self, foods):
        cur=self.root

        for food in foods:
            if food not in cur:
                cur[food]=dict()
            cur=cur[food]
        cur[0]=True

    def travel(self,level,cur):
        if 0 in cur:
            return

        children=sorted(cur)

        for child in children:
            print('--'*level+child)
            self.travel(level+1,cur[child])

n=int(sys.stdin.readline().strip())
nest=Trie()
for _ in range(n):
    input_word=sys.stdin.readline().split()
    k=input_word[0]
    foods=input_word[1:]
    nest.add(foods)
nest.travel(0,nest.root)