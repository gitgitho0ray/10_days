n=10

nums='10 40 30 50 20 10 40 30 50 20'.split()
w='1 2 3 4 5 6 7 8 9 10'.split()
#hacker rank inputs 
n=int(input())
nums=[int(i) for i in list(input().split())]
w=[int(i) for i in list(input().split())]

#weighted mean
wmean=sum([n*w for n,w in zip(nums,w)])/sum(w)
print("{:.1f}".format(wmean))