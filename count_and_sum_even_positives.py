def count_and_sum_even_positives(numbers):
    count = 0
    total_sum = 0

    for num in numbers:
        if num > 0 and num % 2 == 0:
            count += 1
            total_sum += num

    return count, total_sum
