def is_prime(func):  # декоратор
    def wrapper(a, b, c):
        result = func(a, b, c)
        lis = []
        for i in range(1, result + 1):  # цикл определяет к какому виду чисел отнести result
            k = result / i
            if k.is_integer():
                lis.append(k)
        if len(lis) == 2:
            return f"Число(цифра) {result} простое(ая)"
        else:
            return (f"Число(цифра) {result} составное(ая)")

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)






# def is_prime(x):
#     lis = []
#     for i in range(1, x + 1):
#         k = x / i
#         if k.is_integer():
#             lis.append(k)
#     if len(lis) == 2:
#         print(f"Число(цифра) {x} простое(ая)")
#     else:
#         print(f"Число(цифра) {x} составное(ая)")
#
#
#
# for i in range(1, 1000):
#     is_prime(i)