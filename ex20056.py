import sys
n,m,k=map(int,sys.stdin.readline().split())
fb=[]
for _ in range(m):
    arr=list(map(int,sys.stdin.readline().split()))
    fb.append(arr)
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
def move(prv):
    post=dict()
    for key in prv.keys():
        balls=prv[key]
        x=key[0]
        y=key[1]
        for ball in balls:
            m,s,d=ball[0],ball[1],ball[2]
            nx=(x+dx[d]*s)%n
            ny=(y+dy[d]*s)%n
            post_key=(nx,ny)
            if post_key in post.keys():
                post[post_key].append(ball)
            else:
                post[post_key]=[ball]
    del_list=[]
    for key in post.keys():
        balls=post[key]
        ball_sum=len(balls)
        if ball_sum<2:
            continue
        m_sum=0
        s_sum=0
        odd,even=0,0
        for ball in balls:
            m,s,d=ball[0],ball[1],ball[2]
            m_sum+=m
            s_sum+=s
            if d%2==0:
                even+=1
            else:
                odd+=1
        if m_sum//5==0: #m_sum is 0
            del_list.append(key)
        else:
            m=m_sum//5 # 1
            s=s_sum//ball_sum # 2
            post[key]=[]
            if odd==0 or even==0: #3
                dir_arr=[0,2,4,6]
            else:
                dir_arr=[1,3,5,7]
            for i in range(4):
                post[key].append([m,s,dir_arr[i]])
    for item in del_list: # 4
        del post[item]
    return post
fb_dic=dict()
for f in fb:
    r,c,m,s,d=f[0],f[1],f[2],f[3],f[4]
    fb_dic[(r,c)]=[[m,s,d]]
for _ in range(k):
    fb_dic=move(fb_dic)
ans=0
for k in fb_dic.keys():
    for item in fb_dic[k]:
        ans+=item[0] # 5
print(ans)