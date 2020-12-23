#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)

strings = [str(re) for re in res ]

a_res = "".join(strings)
num = int(a_res)

print(num)