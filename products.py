# 1st article : expense notes
products = []
while True:
	name = input('please type item name : ')
	if name == 'q':
		break
	price = input('please type utem price :')
	price = int(price)
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

with open('products.csv', 'w', encoding='utf-8' ) as f:
	#f.write('商品' + ',' + '價格' + '\n')
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		

