from state import *
# import state

def main():
    print("Size Of Maze: ")
    n=12
    starting=[0,0]
    ending=[11,11]
    value_iteration(n,starting,ending)




# implements the value_iteration method
def value_iteration(n,starting,ending):
    for i in range(n):
        for j in range(n):

            s=state(0,i,j)
            state.Array_States[(i,j)]=s
    # print(state.Array_States)
    max=10
    parameter=0.1
    k=0
    max2=0
    p=0
    while(max>parameter and p<=10000):
        max2 = 0
        for i in range(n):
            for j in range(n):
                if(i==ending[0] and j==ending[1]):
                    continue
                st=state.Array_States[(i,j)]
                New_v = -1 + state.Array_States[st.state_transition(0, i, j, n)].value
                New_action=0
                for action in [1,2,3]:
                    v= -1+state.Array_States[st.state_transition(action,i,j,n)].value
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


        p+=1









def print_maze(k,n):
    print("-------------------------")
    print("iteration: "+str(k))
    # print("")
    print("")
    for i in range(n):
        print("||", end=" ")
        for j in range(n):
            m="        "
            L=str(state.Array_States[(i, j)].value) + " : " + value(state.Array_States[(i, j)].optimal_action)
            for i in range(len(L)):
                m=m[:i+1]+L[i]+m[i+2:]
            print(m,
                  end=" || ")
        print("")
        # print("")

def value(i):
    if(i==0):
        return "←"
    if(i==1):
        return "→"
    if(i==2):
        return "↑"
    if(i==3):
        return "↓"


if __name__ == '__main__':
    main()
