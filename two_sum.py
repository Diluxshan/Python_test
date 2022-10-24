def two_sum(arr,targ):
    vari = {}
    for n,x in enumerate(arr,1):
        try:
            return vari[x], n
        except KeyError:
            vari.setdefault(targ - x,n)

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
print("Finished..!")