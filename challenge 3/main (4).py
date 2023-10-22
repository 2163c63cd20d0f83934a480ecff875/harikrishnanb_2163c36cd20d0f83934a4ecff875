"""
write a function called linear_search_product that takes the list of product and a traget product
name as input . the function should perfrom alinear search to find """ the traget product in the list and
return alist  of indicate of all occurrence of the product if found, or an empty list if the product  is not 
found
"""


def linearsearchproduct(productlist ,targetproduct):
indices = []

for index, product in enumerate(productlist):
if product=== targetproduct:
indices.append(index)

return indices


#example usasge:
product=["shoes","boot","loafer"]
target= "shoes"
traget= 'apple'
result= linearsearchproduct(product,traget)
print(result)
