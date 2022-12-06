import os # operating system

#read file
products = []
if os.path.isfile('products.csv'): # check if file is existed
	print('file is ok ! ')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過,繼續下一個
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
	
else:
	print('file is not found ! ')


# let user type expense notes
while True:
	name = input('please type item name : ')
	if name == 'q':
		break
	price = input('please type utem price :')
	price = int(price)
	products.append([name,price])

# print all product and price
for p in products:
	print(p[0], ' price is ', p[1])

# writing file
with open('products.csv', 'w', encoding='utf-8' ) as f:
	#f.write('商品' + ',' + '價格' + '\n')
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
	