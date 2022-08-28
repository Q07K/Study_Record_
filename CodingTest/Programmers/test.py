# TEST
num = 10
size_ = 20
print(f'{num:4f}')
print(str.format(f'{num:^{size_}}'))

print(f'{num:#={size_}}')


print(f'{.86:.2%}')

num1 = 1
num2 = 1.1
print(f'')


n, m = map(int, "3 16".split())

sieve = [0, 0] + [1]*(m-1)
print(sieve)
for i in range(2, m+1):
    if sieve[i]:
        for j in range(i+i, m+1, i):
            sieve[j] = 0
        if i >=n:
            print(i)
            
            