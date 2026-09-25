car = 'subaru'
age = 22
name = 'Alice'
score = 95
is_weekend = True
has_homework = False
fruits = ['apple', 'banana', 'cherry']

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("\nIs name == 'alice'? I predict False.")
print(name == 'alice')

print("\nIs age == 22? I predict True.")
print(age == 22)

print("\nIs age == 30? I predict False.")
print(age == 30)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age != 22? I predict False.")
print(age != 22)

print("\nIs score > 90? I predict True.")
print(score > 90)

print("\nIs score < 50? I predict False.")
print(score < 50)

print("\nIs score >= 95? I predict True.")
print(score >= 95)

print("\nIs score <= 50? I predict False.")
print(score <= 50)

print("\nIs is_weekend and not has_homework? I predict True.")
print(is_weekend and not has_homework)

print("\nIs is_weekend and has_homework? I predict False.")
print(is_weekend and has_homework)

print("\nIs is_weekend or has_homework? I predict True.")
print(is_weekend or has_homework)

print("\nIs (not is_weekend) or has_homework? I predict False.")
print((not is_weekend) or has_homework)

print("\nIs 'apple' in fruits? I predict True.")
print('apple' in fruits)

print("\nIs 'grape' in fruits? I predict False.")
print('grape' in fruits)

print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)

print("\nIs 'apple' not in fruits? I predict False.")
print('apple' not in fruits)
