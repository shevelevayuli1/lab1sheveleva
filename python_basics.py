"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    s=0
    for character in text.lower():
        if character in 'aeiou':
            s+= 1
    return s

print(count_vowels(TextInput(value='Hello World')))
print(count_vowels(TextInput(value='My name is Yulia!')))

def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    return len(text) == len(set(text))

print(has_unique_characters(TextInput(value = 'Hello World')))
print(has_unique_characters(TextInput(value = 'qwertyu')))

def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    return bin(number).count('1')

print(count_one_bits(PositiveIntegerInput(value = 200)))
print(count_one_bits(PositiveIntegerInput(value = 67)))

def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    a = 0
    number = data.value
    while number>9:
        s = 1
        for i in str(number):
            s*= int(i)
        number = s 
        a+=1
    return a

print(multiplicative_persistence(PositiveIntegerInput(value = 39)))
print(multiplicative_persistence(PositiveIntegerInput(value = 4)))

def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    s=0
    for i in range(len(predicted)):
        s += (predicted[i] - expected[i])**2 
        a = s / len(predicted)
    return a

print(mse(VectorPairInput(predicted = [1,2,3], expected = [1,2,3])))
print(mse(VectorPairInput(predicted = [1,2,3], expected = [4,5,6])))
print(mse(VectorPairInput(predicted = [0,0,0], expected = [0,0,0])))


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    s = []
    a = 2
    while a * a <= number:
        if number % a == 0:
            c = 0
            while number % a == 0:
                c += 1
                number //= a
            if c == 1:
                s.append(f"({a})")
            else:
                s.append(f"({a}**{c})")
        a += 1  
    if number > 1:
        s.append(f"({number})")
        
    return "".join(s)

print(prime_factorization(PositiveIntegerInput(value=86240)))
print(prime_factorization(PositiveIntegerInput(value=345)))


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    k = 1
    all = 0
    while all < cube_count:
        all += k ** 2
        if all == cube_count:
            return k
        k += 1
    return "It is impossible"

print(pyramid(PositiveIntegerInput(value=30)))
print(pyramid(PositiveIntegerInput(value=15)))


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    s = str(number)
    l = len(s)
    if l <= 2:
        return True    
    if l % 2 == 0:
        c = 2
    else:
        c = 1     
    d = (l - c) // 2
    left = s[:d]
    right = s[d + c:]
    sleft = sum(map(int, left))
    sright = sum(map(int, right))
    return sleft == sright

print(is_balanced_number(PositiveIntegerInput(value=1234006)))
print(is_balanced_number(PositiveIntegerInput(value=123456)))
