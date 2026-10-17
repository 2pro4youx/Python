print([i for i in range(10)])
print([i for i in range(10) if i % 2 == 0])

print("\n")
func = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in func:
    print(i())