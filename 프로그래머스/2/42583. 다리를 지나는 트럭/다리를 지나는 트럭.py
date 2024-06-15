def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck=0
    st=[]
    for i in range(len(truck_weights)):
        while True:
            if len(st)==0:
                st.append(truck_weights[i])
                truck+=truck_weights[i]
                answer+=1
                break
            elif len(st)<bridge_length:
                if truck+truck_weights[i]<=weight:
                    st.append(truck_weights[i])
                    truck+=truck_weights[i]
                    answer+=1
                    break
                else:
                    st.append(0)
                    answer+=1
            if len(st)==bridge_length:
                truck-=st[0]
                st.pop(0)
    answer+=bridge_length 
    return answer