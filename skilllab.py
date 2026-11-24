'''a=3+5j
print(a)
a=6j
print(a)
a='GOOD MORNIN'
print(a)


c='hi'
print(c)

a="happy day"
print(a)'''


'''a=[10,2.4,False,5j,'hi',[1,2],(1,2),{1,2}]
print(a)
a.pop()
print(a)
a.pop(0)
print(a)'''

'''a=10,100,1000
print(a)
a=(10)
print(a,type(a))
a=(20,)
print(a,type(a))
a=(10,20,30,40)
print(a[2])


a={1,2,3,4}
print(a)'''




'''a={'a':10}
print(a['a'])
p={'a':10,'a':20}
print(p)'''
'''a={'a':[10,20,30],'b':40}
print(a['a'][1])
print(a['a'][-2])'''


'''a='Hello'
print(a[2:3])
print(a[2:3+1:1])
print(a[-2:-3+1:1])
print(a[-3:-2+1:1])
print(a[-1:-4+2:2])
print(a[-1:-5+3:1])'''

'''a='rnin'
print(a[2:3])
print(a[1:3+2])
print(a[-3:-2+2:1])
print(a[0:3+3:1])
print(a[-1:-4+3:-1])'''

'''print(a[::-1])'''

'''a='purvika'
print(a[::-1])
print(a[1:5+1:2])'''

'''a='GOOD MORNING'
print(a[1:5+1:2])
print(a[0:11+1:2])
print(a[-7::3])
print(a[-2:-8-1:-3])
print(a[10:4-1:-3])
print(len(a[-2:-8-1:-3]))'''

'''a=('input')
print(a)'''

'''a=list(input("enter:"))
print(a,type(a))
a=(input("enter:"))
print(type(a))'''
'''a=float(input("enter:"))
print(type(a))
a=int(input("enter:"))
print(type(a))'''

'''a=eval(input("enter:"))
print(a,type(a))'''

'''a=int(input("enter a number:"))
if(a%2==0):
    print('even')
else:
    print('odd')'''
'''list=eval(input('Enter:'))
if len(list)==5:
    print('yes')
else:
    print('no')'''

'''print(ord('a'))
print(ord('z'))
print(ord('A'))
print(chr(ord('A')+32))
print(chr(ord('a')-32))'''

'''ch=(input('Enter:'))
if"A"<=ch<="Z":
    print('upper')
elif"a"<=ch<='z':
    print('lower')
else:
    print('not an alpha')'''

'''username=input("enter:")
if username=='poorvi':
    print('valid username')
else:
    print('invalid username')
passward=input("enter:")
if passward=='123':
        print('you are ready to login')
else:
       print('invalid passward!!')'''



'''i=1
while i<=100:
    print(i)
    i+=1'''

'''i=2
while i<=50:
    print(i)
    i+=2'''
'''n=int(input("Enter num:"))
rev=0
while n>0:
    Id=n%10
    n=n//10
    rev=rev*10+Id
print(rev)'''
'''for i in range(1,11):
    print(i)'''
'''L=[1,2,3]
for i in L:
    print(i)'''

'''s=input('enter:')
out=''
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
        print(out)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()'''
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('4',end=' ')
        else:
            print('@',end=' ')
    print()



    












