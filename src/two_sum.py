def two_sum(numList, target):
    for num in numList:
        diff = target - num
        if diff in numList:
            return num, diff
        return "Not found"
        
if __name__ == '__main__':
    a = [1,9,5,6]
    target = 10
    test = 10
    print two_sum(a, target)