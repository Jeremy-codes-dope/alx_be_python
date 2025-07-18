pattern_size = input("Enter the size of the pattern: ")
i = 1
while i <= int(pattern_size):
    for j in range(1, int(pattern_size) + 1):
        print("*" ,end="")
    print()
    i += 1
        
