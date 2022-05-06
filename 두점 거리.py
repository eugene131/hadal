d_min=0
p_1=[]
p_2=[]

def Swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def x_sort(coo,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if int(coo1[i][0])>int(coo1[j][0]):
                coo1[i],coo1[j]=Swap(coo1[i],coo1[j])
    return coo1

def y_sort(coo,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if int(coo1[0][i])>int(coo1[0][j]):
                coo1[i],coo1[j]=Swap(coo1[i],coo1[j])
    return coo1

def colen(coo1):
    for i in range(0,int(len(coo1))):
        for j in range(i+1,int(len(coo1))):
            coo1[i][0]

def find_min_eazy(coo,n):
    a = int(input())
    lenx = []
    leny = []
    min_len = []
    len1 = float('inf')
    # print(coo)
    for j in range(0, len(coo)):
        for i in range(j + 1, len(coo)):
            x = ((int(coo[j][0]) - int(coo[i][0])) ** 2)
            y = ((int(coo[j][1]) - int(coo[i][1])) ** 2)
            if len1 > (x + y):
                len1 = x + y
    return len1
def dev_list(lst,n):
    lst1=[]
    lst2=[]
    for i in range(0,n/2):
        lst1.append(lst[i])
    for i in range(n/2,n):
        lst2.append(lst[i])
    return lst1,lst2

def find_min(coo1,n):
    if(n<5):
        find_min_eazy(coo1)
    coo1_1,coo1_2=dev_list(coo1)
    dl1,dl2,dl_min = find_min(coo1_1,n/2)
    dr1,dr2,dr_min = find_min(coo1_2,n-(n/2))
    if dl_min<=dr_min:
        p_1=dl1
        p_2=dl2
        d_min=dl_min
    else:
        p_1 = dr1
        p_2 = dr2
        d_min=dr_min
    coo1=y_sort(coo1,n)
    for i in range(0,n-1):
        if (coo1[i+1][0]-coo1[i][0])<2*d_min & coo1[i+1][1]-coo1[i][1]<d_min:
            len1 = float('inf')
            # print(coo)
            for j in range(0, 5):
                for k in range(j + 1, 5):
                    x = ((int(coo1[j][0]) - int(coo1[k][0])) ** 2)
                    y = ((int(coo1[j][1]) - int(coo1[k][1])) ** 2)
                    if len1 > (x + y):
                        len1 = x + y

if __name__ == '__main__':
    a = int(input())
    b=[]
    coo1=[]
    len1=[]
    min_len=[]
    for i in range(0, a):
        b=list(map(int, input().split()))
        coo1.append(b)
    print(coo1)
    coo1=x_sort(coo1,a)
    print(coo1)
    d=int((int(coo1[0][0])+int(coo1[len(coo1)-1][0])))
    print(d)
    find_min(coo1,coo1[0][0],coo1[len(coo1)-1][0],d)



    #특이성 -> situation
    #일관성 -> time
    #합의성 -> other person
    #토할거 같다 ㄹㅇ