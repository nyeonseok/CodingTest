n=int(input())

sub=0
sum, hap =0, 0

for i in range(1, n-1):
    hap = i**2 - sub
    sum+=hap
    sub=hap
    
print(sum)
print(3)
