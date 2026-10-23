def find_largest(numbers):
    if not numbers:
        return none

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
print(find_largest([5, 70, 90, 4]))
              

def find_smallest(numbers):
    if not numbers:
        return none

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
print(find_smallest([5, 70, 90, 4]))                

