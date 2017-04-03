from state import *
# import state

def main():
    print("Goal: ")
    n=101
    p=0.4

    value_iteration(n,p)
# implements the value_iteration method
def value_iteration(n,p):
    for i in range(n):
        if(i==n-1):
            s = state(1, i)
            state.Array_States[i] = s
            continue
        # if(i==0):
        #     s = state(-1, i)
        #     state.Array_States[i] = s
        #     continue
        s=state(0,i)
        state.Array_States[i]=s
    # print(state.Array_States)
    max=10
    parameter=10**(-(10**10))
    k=0
    while(max>parameter):
        max2 = 0
        for i in range(n):
            if(i==0 or i==n-1):
                continue
            st=state.Array_States[i]
            t=min(i,n-i-1)
            New_v =p*state.Array_States[i+1].value+(1-p)*state.Array_States[i-1].value
            New_action=1
            for action in range(t,2,-1):
                v= p*state.Array_States[action+i].value+(1-p)*state.Array_States[i-action].value
                if(v>New_v):
                    New_v=v
                    New_action=action
            if(max2<abs(st.value-New_v) ):
                max2=abs(st.value-New_v)
            st.value=New_v
            st.optimal_action=New_action
        k+=1
        print_maze(k,n)
        max = max2
        # print("max="+str(max2))
    L=[]
    kk=[]
    for i in range(n):
        L.append(state.Array_States[i].optimal_action)
    for i in range(n):
        kk.append(state.Array_States[i].value)
    print(kk)










def print_maze(k,n):
    print("")
    print("iteration: ",k)
    for i in range(n):
        print("||", end=" ")
        print("capital: "+str(i)+ ","+str(state.Array_States[i].value) + "," + str(state.Array_States[i].optimal_action),
                  end=" || ")
        print("")
    print("-------------------------")



if __name__ == '__main__':
    main()
