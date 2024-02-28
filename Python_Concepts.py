#%%
#Inter change position from starting to end
list1=[23,45,67,87,89]
print('old list1={}'.format(list1))

list1[0],list1[-1]=list1[-1],list1[0]

print('new list',list1)


    

# %%

list1=[23,45,67,87,89]
print('old list1={}'.format(list1))

temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp

print('new list',list1)

# %%
list1=[23,45,67,87,89]
print('old list1=',*list1)
# print(type(*list1))

# %%
list1=[23,45,67,87,89]

a,*b,c,d=list1

print(a,*b,c,d)

# %%
