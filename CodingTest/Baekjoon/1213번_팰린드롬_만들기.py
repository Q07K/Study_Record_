input_str = input()
dict_ = {}
for i in input_str:
    try:
        dict_[i] += 1
    except:
        dict_.update({i: 1})

print(dict_)

search = sorted(dict_.values(), key=lambda x: x % 2)
if search[-1]%2 and search[-2]%2:
    print("I'm Sorry Hansoo")
else:

    
