def mirrored_right_angle_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * i)

rows = 5
mirrored_right_angle_triangle(rows)
