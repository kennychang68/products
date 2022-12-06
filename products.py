
# reading file
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #跳過,繼續下一個
		#s = line.strip().split(',')
		#name = s[0]
		#price = s[1]
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)

# 1st article : expense notes
##products = [] ; already move above
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
		

