import sys

binary = ''
#def toBin(num, binary):
def toBin(num):
    global binary
    quotient = num // 2
    binary = str(num % 2) + binary
    if quotient != 0:
##        toBin(quotient, binary)
        toBin(quotient)
        
    return binary

def toDec(num):
    decimal = 0
    for x in range(len(arr)):
        if arr[x] == 1:
            decimal += 2**(len(arr)-(x+1))
            
    return decimal

def addBin(num1, num2):
    if len(str(num2)) > len(str(num1)):
        x = num2
        num2 = num1
        num1 = x
    

    return binSum
if __name__ == "__main__":
    while True:
        op = int(input("1. Convert decimal to binary\n2. Convert binary to decimal\n3. Add binary numbers.\n4. Exit\n"))
        if op == 1:
            num = int(input("Decimal number to convert to binary? "))
            arr = [int(i) for i in str(num)]
##            binary = ''
##            binary = toBin(num, binary)
            binary = toBin(num)
            print(str(num), "in binary is", str(binary))
            binary = ''
        elif op == 2:
            num = int(input("Binary number to convert to decimal? "))
            arr = [int(i) for i in str(num)]
            decimal = toDec(num)
            print(str(num), "in decimal is", str(decimal))
        elif op == 3:
            num1 = int(input("First number: "))
            num2 = int(input("Second number: "))
            binSum = addBin(num1, num2)
            print(str(num1), "+", str(num2), "=", str(binSum))
        elif op == 4:
            sys.exit("Killed")
            #exit()
        else:
            print("Invalid input, try again")
            



