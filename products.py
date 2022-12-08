import os # operating system

#read file
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #跳過,繼續下一個
            name, price = line.strip().split(',')
            products.append([name,price])
    return products



# let user type expense notes
def user_input(products):
    while True:
        name = input('please type item name : ')
        if name == 'q':
            break
        price = input('please type item price :')
        price = int(price)
        products.append([name,price])
    return products

# print all product and price
def print_products(products):
    for p in products:
        print(p[0], ' price is ', p[1])

# writing file
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8' ) as f:
        #f.write('商品' + ',' + '價格' + '\n')
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
    



def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('file is ok ! ')
        products = read_file(filename)
    else:
        print('file is not found ! ')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()


