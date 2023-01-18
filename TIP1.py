n = int(input())
a = []

for i in range(2**n):
    s = str(input())
    a.append(list(map(int, s.split())))

def treug(a):

    z = []
    clmn = []

    for i in range(2 ** n):
        clmn.append(a[i][n])

    while len(clmn) > 0:
        z.append(clmn[0])

        for j in range(len(clmn)-1):
            clmn[j] = (clmn[j] + clmn[j+1]) % 2

        clmn.pop()

    return z

def zhgl(z):
    str = ''
    if z[0]==1:
        str += '1 + '
    for i in range(1, len(z)):
        if (str != '') and (z[i]==1):
            str += ' + '
        for j in range(1, n+1):
            if (z[i]==1) and (i % 2**j >= 2**(j-1)):
                str += chr(65+n-j)
    return str

z = treug(a)
polinom = zhgl(z)

print(z)

print(polinom)