pattern_size = int(input("Enter the size of the pattern: "))
i = 1
while i <= pattern_size:
    for j in range(1, pattern_size + 1):
        print("*" ,end="")
    print()
    i += 1
        
