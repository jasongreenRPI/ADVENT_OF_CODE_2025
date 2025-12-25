import os


def shouldAddThisId(id):
    # id should be added if it is made only of some sequence of digits repeated twice

    # case 1: Odd
        # Not possible because 2k = 3 , k = 2/3 so invalid not whole number
    
    # case 2: Even

    length = len(id)

  
    for i in range(1 , length // 2 + 1):
        res = length % i

        if res == 0:

          res = checkIdWithStep(id,i)

          if checkAllElementsEqual(res):
              return True
          

        else:
            continue
    return False

def checkAllElementsEqual(lis):
    first = lis[0]

    for i in range(1,len(lis)):
        if lis[i] != first:
            return False
        
    return True

def checkIdWithStep(id,step):
    lis = []
    for i in range(0, len(id), step):
        cur = id[i:i+step]
        lis.append(cur+"")
    return lis

def openAndSeedList(filename , dir):
    lis = []
    with open(dir + "/" + filename, 'r') as f:
        for line in f:
            split = line.split(',')

            for item in split:
                lis.append(item)

    return lis

def parseInputModifyAcc(inputs):
    res = 0
    for input in inputs:
        splitted = input.split('-')
        range1,range2 = int(splitted[0]), int(splitted[1])

        for i in range(range1,range2+1):
            
            toCheck = str(i)

            shouldAdd = shouldAddThisId(toCheck)

            if shouldAdd:
            #    print("HI", i, res)

                res+= i
    return res

def main():
    
    cwd = os.getcwd()
    
   # inputs = openAndSeedList("input.txt", cwd)
    inputs = openAndSeedList("input.txt", cwd)

    res = parseInputModifyAcc(inputs)
    print(res)


if __name__ == "__main__":
    main()


#1227775554
#21898734247