print((lambda x: x**2)(2))

# takes two int, returns mean of them
print((lambda x, y: (x+y)/2)(3, 5))


# You can also assign the lambda statement in parentheses
# to a variable :
average = (lambda x, y: (x+y)/2)(3, 5)
print(average)


# Alternatively, you can assign the lambda function definition
# to a variable then you can call it
def average(x, y): return (x+y)/2


print(average(3, 5))


############################################
# Lambda within Built-in (map()) Functions-1
############################################

# The basic formula syntax is : map(function, iterable)

iterable = [1, 2, 3, 4, 5]
map(lambda x: x**2, iterable)
print(list(map(lambda x: x**2, (1, 3, 5))))
result = map(lambda x: x**2, iterable)

print(type(result))  # it's a map type
print(list(result))  # we've converted it to list type to print
print(list(map(lambda x: x**2, iterable)))  # you can print directly

# Note that map() takes each element from iterable objects one by one
# and in order.
letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']
numbers = map(lambda x, y, z: x+y+z, letter1, letter2, letter3)

print(list(numbers))
#Output : ['one', 'six', 'ten', 'two']


# Multiplying numbers in a list
number_list = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 3, number_list))
print(result)


###############################################
# Lambda within Built-in (filter()) Functions-2
###############################################

# The basic formula syntax is : filter(function, sequence)
# Note that filter() filters each element in the iterable object,
# depending on whether the function's result is True or False.

first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda x: x % 2 == 0, first_ten)
print(type(even))  # it's 'filter' type,
# in order to print the result,
# we'd better convert it into the list type

print('Even numbers are :', list(even))


# filter the vowels from the first ten letters in the list
vowel_list = ['a', 'e', 'i', 'o', 'u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

vowels = filter(lambda x: True if x in vowel_list else False, first_ten)

print('Vowels are :', list(vowels))


# Another Example
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: True if x <= 6 else False, number_list))
print(result)


###############################################
# Lambda within User-Defined Functions
###############################################

def modular_function(n):
    return lambda x: x ** n


power_of_2 = modular_function(2)  # first sub-function derived from def
power_of_3 = modular_function(3)  # second sub-function derived from def
power_of_4 = modular_function(4)  # third sub-function derived from def

print(power_of_2(2))  # 2 to the power of 2
print(power_of_3(2))  # 2 to the power of 3
print(power_of_4(2))  # 2 to the power of 4

print(modular_function(2)(2))
print(modular_function(3)(2))
print(modular_function(4)(2))


def repeater(n):
    return lambda x: x * n


repeat_2_times = repeater(2)  # repeats 2 times
repeat_3_times = repeater(3)  # repeats 3 times
repeat_4_times = repeater(4)  # repeats 4 times

print(repeat_2_times('alex '))
print(repeat_3_times('lara '))
print(repeat_4_times('linda '))

print(repeater(2)('alex '))
print(repeater(2)('lara '))
print(repeater(2)('linda '))

for i in [1, 2, 3, 4]:
    print(i, ":", (lambda x: "odd" if x % 2 != 0 else "even")(i))


def hipotenus(a, b): return (a**2 + b**2) ** 0.5


hipotenus(3, 4)


# Example
num1 = [9, 6, 7, 4]
num2 = [3, 6, 5, 8]
a = map(lambda x, y: (x+y)/2, num1, num2)
print(list(a))


# Example
w1 = ["you", "much", "hard"]
w2 = ["i", "you", "you"]
w3 = ["love", "ate", "work"]
text = map(lambda x, y, z: x + " " + y + " " + z + " ", w2, w3, w1)
for i in (text):
    print(i)

# Example
words = ["apple", "swim", "clock", "me", "kiwi", "banana"]
for i in filter(lambda x: len(x) < 5, words):
    print(i)


# Example
vowel_list = ["a", "e", "i", "o", "u"]
first_ten = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
vowels = filter(lambda x: True if x in vowel_list else False, first_ten)
# OR vowels = filter(lambda x: if x in vowel_list, first_ten)
print(list(vowels))


# Example
def functioner(emoji=None):
    return lambda message: print(message, emoji)


(lambda message: print(message, ":)"))(66)
(lambda message: print(message, ":)"))([66])
print_smile = functioner(":)")
print_sad = functioner(":(")
print_neutral = functioner(":|")
print(print_smile("Hello"))
print(print_sad("bugünkü dersteki yüz ifadem -->"))
print(print_neutral("Hello"))


# Another Usage
a = (lambda x: print(x))(33+22)
print(a)


# Example
def func_generator(func_name):
    return lambda x: func_name(x)


ofd_print = func_generator(print)
ofd_max = func_generator(max)
ofd_bool = func_generator(bool)
ofd_sorted = func_generator(sorted)

print(ofd_print("Hello"))
print(ofd_max([35, 75]))
print(ofd_bool(35))
print(ofd_sorted(["x", "c"]))
