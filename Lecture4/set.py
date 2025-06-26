# set is a collection of the unordered items 
#  each element in the set must be unique & immutable 
nums={1,3,4,"hello","hello","world"}
print(nums)
empty_set={ } # it is empty dictionary
empty_set=set()

nums.add(44)
nums.remove(44)
nums.pop() # remove random value
# nums.clear()
nums2={403,3893,4,2}
print(nums.union(nums2))
print(nums)
print(nums2.intersection(nums))

values={9,9.0}
print(values) # gives {9}
values={9,"9.0"}
print(values)
values={("int",9),("float",9.0)}
print(values)

