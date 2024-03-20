import math

# 1 задание
"""
def get_end(n):
    last_digit = n % 10
    if last_digit == 1 and n % 100 != 11:
        return "программист"
    elif 2 <= last_digit <= 4 and (n % 100 < 12 or n % 100 > 14):
        return "программиста"
    else:
        return "программистов"


def main():
    n = int(input("Введите количество программистов: "))
    print(f"{n} {get_end(n)}")


if __name__ == "__main__":
    for i in range(10):
        main()
"""

# 2 задание
"""
def get_sum(numbers):
    rst = []
    for i in range(len(numbers)):
        if i == 0:
            left_neighbor = numbers[-1]
        else:
            left_neighbor = numbers[i - 1]
        if i == len(numbers) - 1:
            right_neighbor = numbers[0]
        else:
            right_neighbor = numbers[i + 1]
        rst.append(left_neighbor + right_neighbor)
    return rst


def main():
    numbers = [int(x) for x in input("Введите список чисел через пробел").split()]
    if len(numbers) == 1:
        print(numbers[0])
    else:
        print(" ".join(map(str, get_sum(numbers))))


if __name__ == "__main__":
    main()
"""

# 3 задание
"""
def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while num <= n * n:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


def print_matrix(matrix):
    max_num_width = len(str(len(matrix) * len(matrix[0])))
    for row in matrix:
        print(" ".join(str(num).rjust(max_num_width) for num in row))


def main():
    n = int(input("Введите размер матрицы: "))
    spiral_matrix = generate_matrix(n)
    print("Спиральная матрица размером", n, "x", n, ":")
    print_matrix(spiral_matrix)


if __name__ == "__main__":
    main()
"""

# 4 задание
"""
def check_password(password):
    if len(password) < 10:
        print("Ненадежный пароль")
        return

    digit_count = sum(1 for char in password if char.isdigit())
    uppercase_count = sum(1 for char in password if char.isupper())
    special_count = sum(1 for char in password if char in "!@#$%*")

    if digit_count >= 3 and uppercase_count >= 1 and special_count >= 1:
        print("Хорош!!!")
    else:
        print("Ненадежный пароль")


def main():
    password = input("Введите пароль: ")
    check_password(password)


if __name__ == "__main__":
    main()
"""

# 5 задание
"""
def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def get_fibonacci_numbers(n):
    if not isinstance(n, int):
        raise ValueError("n должен быть целым числом")
    if n < 0:
        raise ValueError("n должен быть неотрицательным")
    fibonacci_numbers = [0, 1]
    for i in range(2, n + 1):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers


def main():
    try:
        text = input("Введите количество чисел Фибоначчи: ")
        if not is_number(text):
            raise ValueError("Введено не число")
        n = int(text)
        fib_numbers = get_fibonacci_numbers(n)
        for i in range(1, n + 1):  
            print(f"Fibonacci Numbers №{i}: {fib_numbers[i - 1]}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
"""


# 6 задание
"""

def print_square_table():
    print("     ", end="")
    for i in range(10):
        print(f"{i:4}", end="")
    print("\n" + " " * 5 + "-" * 44)
    for i in range(1, 10):
        print(f"{i:2} |", end="")
        for j in range(10):
            num = i * 10 + j
            num = num ** 2
            print(f"{num:4}", end=" ")
        print()


print_square_table()
"""

# 7 задание
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Square:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 4 * self.a


class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


def main():
    # Список фигур
    figures = [
        Rectangle(1, 3),
        Square(2),
        Triangle(1, 2, 2),
        Circle(3),
        Rectangle(2, 3),
        Square(4),
        Triangle(3, 3, 3),
        Circle(5),
    ]

    for figure in figures:
        if isinstance(figure, Rectangle):
            print(f"прямоугольник ({figure.a} х {figure.b}) - {figure.perimeter()}")
        elif isinstance(figure, Square):
            print(f"квадрат (а = {figure.a}) - {figure.perimeter()}")
        elif isinstance(figure, Triangle):
            print(f"треугольник ({figure.a} х {figure.b} х {figure.c}) - {figure.perimeter()}")
        elif isinstance(figure, Circle):
            print(f"круг (г = {figure.r}) - {figure.perimeter()}")


if __name__ == "__main__":
    main()
"""
# 8 задание

"""


def max_diagonals(n):
    if n <= 2:
        return 0
    else:
        return int(0.5 * (n * (n - 3)))


def main():
    n = int(input("Введите количество вершин: "))
    print(f"Максимальное количество диагоналей: {max_diagonals(n)}")


if __name__ == "__main__":
    main()
"""
