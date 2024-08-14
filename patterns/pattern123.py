def create_pyramid_pattern(size):
    double_size = size * 2
    mid_point = size

    
    for i in range(mid_point):
        for j in range(mid_point - i):
            print(" ", end="")

        for j in range(size - i, size + i + 1):
            if j == size - i or j == size + i:
                print("*", end="")
            else:
                print(" ", end="")

        print()

    
    for j in range(0, size * 2 + 1):
        if j == 0 or j == size * 2 - 1:
            print("*", end="")
        elif j == size:
            print(f"{size}", end="")
        else:
            print(" ", end="")

    print()

    
    for i in range(mid_point + 1, double_size):
        for j in range(i - mid_point):
            print(" ", end="")
        for j in range(i - size, double_size - (i - size) + 1):
            if j == i - size or j == double_size - (i - size):
                print("*", end="")
            else:
                print(" ", end="")
        print()

    
    for i in range(size):
        for j in range(double_size + 1):
            print("*", end="")

        print()


def display_pattern():
    try:
        size = int(input("Enter a number (1, 2, or 3): "))
        if size in [1, 2, 3]:
            print(f"Pattern for size = {size}:\n")
            create_pyramid_pattern(size)
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


display_pattern()

