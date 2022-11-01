from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    prime_numbers = []
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        for e in permutations(numbers, i):
            num = int("".join(e))
            if num not in prime_numbers and is_prime(num):
                answer += 1
                prime_numbers.append(num)

    return answer


primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1 :])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer
