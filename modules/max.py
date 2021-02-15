def maxValue(numbers):
    """
    return the maximum value in a list of values
    """
    max = numbers[0]

    for number in numbers:
        if number > max:
            max = number
    return max
