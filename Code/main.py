def cnt(l):
    c=0
    for i in l:
        if i==0:
            c+=1
        else:
            break
    return c
def odr_mat(mtrx):
    min0=0
    fmtrx=[]
    while mtrx!=[]:
        i=0
        while i <(len(mtrx)):
            if cnt(mtrx[i])==min0:
                fmtrx.append(mtrx[i])
                mtrx.pop(i)
            else:
                i+=1
            if mtrx==[]:
                break
        min0+=1
    return fmtrx
def frwd_stp(mtrx, str):
    fmtrx=mtrx
    m=len(mtrx)
    n=len(mtrx[0])
    pvt=1
    found=False
    for i in range(len(fmtrx[str])):
        if fmtrx[str][i]!=0 and not found:
            pvt=fmtrx[str][i]
            pvt_col=i
            found=True
        fmtrx[str][i]=fmtrx[str][i]/pvt
    if not found:
        return fmtrx
    for i in range(str+1, m):
        if fmtrx[i][pvt_col]==0:
            continue
        scal=fmtrx[i][pvt_col]
        for j in range(pvt_col, n):
            fmtrx[i][j]=fmtrx[i][j]-fmtrx[str][j]*scal
            if fmtrx[i][j]>=-1e-10 and fmtrx[i][j]<=1e-10:
                fmtrx[i][j]=0
    return fmtrx
def bckwd_stp(mtrx, bstr):
    fmtrx=mtrx
    if fmtrx[bstr]==[0]*n:
        return fmtrx
    for j in range(n):
        if fmtrx[bstr][j]!=0:
            pvt_coll=j
            break
    for i in range(bstr-1, -1, -1):
        scal=fmtrx[i][pvt_coll]
        for j in range(n):
            fmtrx[i][j]=fmtrx[i][j]-fmtrx[bstr][j]*scal
    return fmtrx
def rref_cal(mtrx):
    m=len(mtrx)
    n=len(mtrx[0])
    fmtrx=odr_mat(mtrx)
    mtrx=fmtrx
    for i in range(m):
        mtrx=frwd_stp(mtrx, i)
    fmtrx=odr_mat(mtrx)
    for i in range(m-1, -1, -1):
        fmtrx=bckwd_stp(fmtrx, i)
    return fmtrx
def p_soln(mtrx):
    non_pvt_cols =  [i for i in range(len(mtrx[0]))]
    found = False
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            if mtrx[i][j]!=0:
                non_pvt_cols.remove((j))
                break
    lol=[]
    for i in non_pvt_cols:
        l=[0]*len(mtrx[0])
        l[i]=1 #[0, 1, 0, 0, 0 , 0]
        n=0
        for x in range(len(l)):
            if x in non_pvt_cols:
                pass
            else:
                l[x]=-mtrx[n][i]
                n+=1
            if x==i:
                break
        lol.append(l)
    return lol
mtrx=[]
f=open("matrices.txt")
while True:
    inpt=f.readline()
    if inpt=="":
        m=len(mtrx)
        n=len(mtrx[0])
        fmtrx=rref_cal(mtrx)
        for i in fmtrx:
            print(i)
        print()
        print("The parametric solution is: ")
        lol = p_soln(fmtrx)
        d = 1
        print("x = ", end="")
        for i in range(len(lol) - 1):
            print("x" + str(d) + str(lol[i]) + " + ", end=" ")
            d += 1
        if len(lol) > 0:
            print("x" + str(d) + str(lol[-1]), end=" ")
        print("\n" + "*" * 50)
        break
    elif inpt=="***\n":
        m=len(mtrx)
        n=len(mtrx[0])
        fmtrx=rref_cal(mtrx)
        for i in fmtrx:
            print(i)
        print()
        print("The parametric solution is: ")
        lol=p_soln(fmtrx)
        d=1
        print("x = ", end="")
        for i in range(len(lol)-1):
            print("x"+str(d)+str(lol[i]) + " + ", end=" ")
            d+=1
        if len(lol)>0:
            print("x" + str(d) + str(lol[-1]), end=" ")
        print("\n"+"*"*50)
        print()
        mtrx=[]
        continue
    else:
        mtrx.append([float(i) for i in inpt.split()])
f.close()
