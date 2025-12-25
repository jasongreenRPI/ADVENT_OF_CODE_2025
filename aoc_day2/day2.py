import os


def shouldAddThisId(id):
    # id should be added if it is made only of some sequence of digits repeated twice

    # case 1: Odd
        # Not possible because 2k = 3 , k = 2/3 so invalid not whole number
    
    # case 2: Even

    length = len(id)

    middle = length // 2


    left = id[0:middle]
    right = id[middle:]

    print(f"id: {id}, l: {left},r: {right}, length: {length}, middle: {middle}")

    if left == right:
        return True
    else:
        return False



def openAndSeedList(filename , dir):
    lis = []
    with open(dir + "/" + filename, 'r') as f:
        for line in f:
            split = line.split(',')

            for item in split:
                lis.append(item)

    return lis


def getFactors(num):
    # 1 -> 1
    # 2 -> 1, 2
    # 3 -> 1, 3
    # 4  > 1, 2, 4
    factors = []

    for i in range(1, num+1):
        res = num / i
        extra = num % i
      #  print(num, i)

        if extra != 0:
            print(f"Not a factor right? num: {num}, i: {i}")
        else:
            print(f"Should be a factor right? num: {num}, i: {i}")
            factors.append(i)
    return factors

def parseInputModifyAcc(inputs, acc):
    
    for input in inputs:
        splitted = input.split('-')
        range1,range2 = int(splitted[0]), int(splitted[1])

        for i in range(range1,range2+1):

            shouldAdd = shouldAddThisId(str(i))
            if shouldAdd:
                acc+=i

def main():
    acc = 0
    cwd = os.getcwd()
    
   # inputs = openAndSeedList("input.txt", cwd)
    inputs = openAndSeedList("input.txt", cwd)

   # parseInputModifyAcc(inputs,acc)
    
 #   print(acc)
    fac8 = getFactors(8)
    fac32 = getFactors(32)
    print(fac32,fac8)

if __name__ == "__main__":
    main()


#1227775554
#21898734247