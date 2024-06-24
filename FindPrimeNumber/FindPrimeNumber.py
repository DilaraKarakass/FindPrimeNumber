def IsPrime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number%i==0:
            return False

    return True


def FindPrimeNumber(number):
    prime_numbers=[]
    for i in range(2,number+1):
        if IsPrime(i):
            prime_numbers.append(i)
    return prime_numbers


number=int(input("Please enter a number:  "))
print(FindPrimeNumber(number))


    

