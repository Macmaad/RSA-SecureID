"""
Macedo Madrigal Rodrigo.
314676797
"""


from random import randint


def generate_random_number():
    """
    Using linear congruential generator, we get 1000000 of numbers and store the
    ones that are bigger or equal to 8 and smaller or equal of 15 on length.

    We just return one of it
    :return:
    """
    a, x_n, c, m, numbers = 1245, 768, 9892, 999999999999999, []
    for i in range(100000):
        x_n_1 = x_n
        x_n = (a * x_n_1 + c) % m
        if 8 <= len(str(x_n)) <= 15:
            numbers.append(x_n)

    return numbers[randint(0, 100000 - 1)]


def check_if_prime(number_):
    """
    Check if the number_ parameter is a prime.

    :param number_: int number
    :return:
    """
    if number_ <= 1:
        return False

    elif number_ <= 3:
        return True

    if number_ % 2 == 0 or number_ % 3 == 0:
        return False

    i = 5
    while i * i <= number_:
        if number_ % i == 0 or number_ % (i + 2) == 0:
            return False
        i += 6

    return True


def max_divisor(r, s):
    """
    Recursive Max divisor algorithm.
    :param r:
    :param s:
    :return:
    """
    if s == 0:
        return r
    else:
        return max_divisor(s, r % s)


def get_power_of_two(exp):
    """
    Needed for powers that are not power of two.
    :param exp: Power value.
    :return: List with the power decomposition on powers of 2.
    """
    exp = bin(exp)
    i = 0
    nums = []
    for digit in str(exp)[2:][::-1]:
        if digit == "1":
            nums.append(2 ** i)
        i += 1
    return nums


def fast_exp_handler(num, e, mod):
    """
    For the cases where the e is not a power of two, we need to get
    the values of it with the number on binary. For this we have  a
    handler to do all the operations.

    After getting the e on binary and the decomposition of power of 2
    we can use the fast_exp function and the multiply all the results
    and get the mod.

    :param num: Number to get the result
    :param e: Exponent of the number
    :param mod: Number that we are getting the module.
    :return: Result of doing the fast exp.
    """
    power_of_two = get_power_of_two(e)
    res = []
    total = 1
    for power in power_of_two:
        res.append(fast_exp(num, power, mod))
    for num in res:
        total *= num
    return total % mod


def fast_exp(num, e, mod):
    """
    Starting with exp = 1 and while it is less than e, we are going to do
    ((num % mod) ** 2) % mod and then we do exp ** 2

    :param num: Number to get the result
    :param e: Exponent of the number
    :param mod: Number that we are getting the module.
    :return: Result of doing the fast exp.
    """
    exp = 1
    num = (num ** exp) % mod
    while exp < e:
        num = ((num % mod) ** 2) % mod
        exp = exp * 2
    return num


print(generate_random_number())
print(check_if_prime(10068833))
print(max_divisor(7 * 7 * 7 * 5 * 4 * 3 * 2 * 12 * 232, 7 * 7 * 7 * 5 * 5 * 5 * 232 * 1))
print(fast_exp_handler(7, 66, 101))
