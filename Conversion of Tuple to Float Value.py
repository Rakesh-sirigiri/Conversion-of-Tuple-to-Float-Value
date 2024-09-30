tup = (2,6)
print("The original tuple : " + str(tup))
res = float('.'.join(str(ele) for ele in tup))
print("The float after conversion from tuple is : " + str(res))
