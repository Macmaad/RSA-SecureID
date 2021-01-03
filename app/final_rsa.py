import random
import time


def is_prime(number: int) -> bool:
    """
    Check if if a number is prime, using the 6k ± 1 optimization. 
    """
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def get_primer_number() -> int:
    """
    Given a 20 bits random number, returns the one that is prime. 
    """
    while True:
        number = random.getrandbits(20)
        if is_prime(number):
            break
    return number


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


def are_coprimes(number: int) -> bool:
    e = 2 ** 16 + 1
    if max_divisor(number, e) == 1:
        return True
    return False


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


def rsa_generator():
    """
    Main handler to generate RSA secure id. 
    """
    p_pseudo_random_1 = get_primer_number()
    q_pseudo_random_2 = get_primer_number()
    mod_n = p_pseudo_random_1 * q_pseudo_random_2
    phi = (p_pseudo_random_1 - 1) * (q_pseudo_random_2 - 1)
    public_key = 2 ** 16 + 1
    while True:
        i = 16
        if max_divisor(public_key, phi) == 1:
            break
        i -= 1
        public_key = 2 ** i + 1
    i = 0
    while True:
        i += 1
        x = 1 + i * phi
        if x % public_key == 0:
            private_key = int(x / public_key)
            break

    return mod_n, public_key, private_key


def generate_values_for_rsa():
    n, public_key, private_key = rsa_main()
    pin = random.randint(1111, 9999)
    encrypted_pin = fast_exp_handler(pin, public_key, n)
    decrypted_pin = fast_exp_handler(encrypted_pin, private_key, n)
    return encrypted_pin, decrypted_pin, pin
