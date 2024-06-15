from collections import deque
def solution(prices):
    answer = []
    """q = deque(prices)
    while q:
        price = q.popleft()
        sec = 0
        for item in q:
            sec+=1
            if price > item:
                break            
        answer.append(sec)
        sec = 0"""
    
    length = len(prices)
    answer = [ i for i in range(length-1,-1,-1)]
    st = [0]
    for i in range(1,length):
        while st and prices[st[-1]] > prices[i]:
            j = st.pop()
            answer[j] = i - j
        st.append(i)
        
    return answer