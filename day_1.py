#Mean, median and mode
n = int(input())
nums = list(input().split())

nums = [int(i) for i in nums]
nums.sort()

# mean
print("{:.1f}".format(sum(nums ) /n))

# median
if len(nums ) % 2= =0:
    print((nums[int((len(nums ) /2 ) -1) ] +nums[int((len(nums ) /2))] ) /2)
else:
    print((nums[int(((len(nums ) +1 ) /2) ) -1]))

# mode
mod e ={}
for i in nums:
    if i in mode.keys():
        mode[i ]+ =1
    else:
        mode[i ] =1
mode_lis t =[]
for i in list(mode.items()):
    if i[1 ]= =max(mode.values()):
        mode_list.append(i[0])
print(mode_list[0])

#weighted mean
n=10
nums='10 40 30 50 20 10 40 30 50 20'.split()
w='1 2 3 4 5 6 7 8 9 10'.split()

#hacker rank inputs
# n=int(input())
# nums=[int(i) for i in list(input().split())]
# w=[int(i) for i in list(input().split())]


wmean=sum([n*w for n,w in zip(nums,w)])/sum(w)
print("{:.1f}".format(wmean))