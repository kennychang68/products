# 1st article : expense notes
products = []
while True:
	name = input('please type item name : ')
	if name == 'q':
		break
	price = input('please type utem price :')
	##p = []
	##p.append(name)
	##p.append(price)
	#p = [name, price]
	#products.append(p)
	products.append([name,price])

#print(products)
#print(products[1][0])

for p in products:
	#print(p)
	print(p[0], ' price is ', p[1])
	#print(p[1])


