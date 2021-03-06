import sys

binary = ''
def toBin(num):
    global binary
    quotient = num // 2
    binary = str(num % 2) + binary
    if quotient != 0:
        toBin(quotient)
        
    return binary

def toDec(num):
    decimal = 0
    for x in range(len(arr)):
        if arr[x] == 1:
            decimal += 2**(len(arr)-(x+1))
            
    return decimal

def addBin(num1, num2):
    binSum = ''
    carry = 0
    if len(num2) > len(num1):
        for i in range(len(num2) - len(num1)):
            num1.insert(0, 0)
    if len(num1) > len(num2):
        for i in range(len(num1) - len(num2)):
            num1.insert(0, 0)
    #Reverse the numbers    
    num1.reverse()
    num2.reverse()
    for x in range(len(num1)):
        if (num1[x] + num2[x] + carry) == 0:
            binSum = '0' + binSum 
            carry = 0
        elif (num1[x] + num2[x] + carry) == 1:
            binSum = '1' + binSum 
            carry = 0
        elif (num1[x] + num2[x] + carry) == 2:
            binSum = '0' + binSum 
            carry = 1
        elif (num1[x] + num2[x] + carry) == 3:
            binSum = '1' + binSum 
            carry = 1
    if carry == 1:
        binSum = '1' + binSum
        
    return binSum


if __name__ == "__main__":
    while True:
        try:
            op = input("1. Convert decimal to binary\n2. Convert binary to decimal\n3. Add 2 binary numbers.\n4. Exit\n")
            if op == '1': #Decimal to binary
                num = int(input("Decimal number to convert to binary? "))
                arr = [int(i) for i in str(num)]
                binary = toBin(num)
                print("\n" + str(num), "in binary is", str(binary) + "\n")
                binary = ''
                
            elif op == '2': #Binary to decimal
                num = int(input("Binary number to convert to decimal? "))
                arr = [int(i) for i in str(num)]
                decimal = toDec(num)
                print("\n" + str(num), "in decimal is", str(decimal) + "\n")

            elif op == '3': #Binary addition
                num1 = input("First number: ")
                num2 = input("Second number: ")
                arr1 = [int(i) for i in str(num1)]
                arr2 = [int(i) for i in str(num2)]
                binSum = addBin(arr1, arr2)
                print("\n" + str(num1), "+", str(num2), "=", str(binSum) + "\n")

            elif op == '4': #Exit
                exit()

            else:
                print("Invalid input, try again")
        except:
            print("\nAn error occured. Please try again.\n")



