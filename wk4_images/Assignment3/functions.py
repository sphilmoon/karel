def multiply(num1, num2):
	product = num1 * num2
	return product # gotta return the product to use multiply function. 

def main():
	num1 = int(input("Type your first number: "))
	num2 = int(input("Type your second number: "))

	product2 = multiply(num1, num2)
	print(product2)

if __name__ == '__main__':
    main()