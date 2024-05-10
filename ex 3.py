dct={
    'a':1,
    'b':2
}
lst1=['c','d']
lst2=[3,4]
for value, x in  (lst1,lst2):
    dct[value]=x
    print(dct)
