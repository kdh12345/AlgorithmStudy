def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length-1, -1, -1)]
    
    st =[0]
    for i in range(1,len(prices)):
        while st and prices[st[-1]] > prices[i]:
            j = st.pop()
            answer[j] = i - j
        st.append(i)
    return answer