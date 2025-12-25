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

def main():
    acc = 0
    cwd = os.getcwd()
    
   # inputs = openAndSeedList("input.txt", cwd)
    inputs = openAndSeedList("input.txt", cwd)


    for input in inputs:
        splitted = input.split('-')
        range1,range2 = int(splitted[0]), int(splitted[1])

        for i in range(range1,range2+1):

            shouldAdd = shouldAddThisId(str(i))
            if shouldAdd:
                acc+=i
    print(acc)
if __name__ == "__main__":
    main()


#1227775554
#21898734247