#std
n=int(input())
nums=input().split()
nums = [int(i) for i in nums]
nums.sort()
mean=sum(nums)/n
std=((sum([(i-mean)**2 for i in nums]))/n)**0.5
print(round(std,1))


def median(data):
    data = [int(i) for i in data]
    data.sort()
    if len(data) % 2 == 0:  # checks if number is even
        return (data[int((len(data) / 2) - 1)] + data[int((len(data) / 2))]) / 2
    else:
        return data[int(((len(data) + 1) / 2)) - 1]


def median_index(data):
    """
    Returns median value index in dataset
    """
    data = [int(i) for i in data]
    data.sort()
    if len(data) % 2 == 0:  # checks if number is even
        print('Dataset contains even number of variables')
    else:
        return int(((len(data) + 1) / 2)) - 1


#quartiles
def quartiles(data):
    """
    Returns list of quartiles (Q1,Q2,Q3)
    """
    if len(data)%2==0:
        quartile2=median(data)
        lower = [i for i in data if float(i) < quartile2]
        upper = [i for i in data if float(i) > quartile2]
        quartile1=median(lower)
        quartile3=median(upper)
        return [quartile1, quartile2, quartile3]
    else:
        quartile2=median(data)
        index=median_index(data)
        lower = data[:index]
        upper = data[index+1:]
        quartile1=median(lower)
        quartile3=median(upper)
        return [float(quartile1), float(quartile2), float(quartile3)]

print(quartiles(s))


