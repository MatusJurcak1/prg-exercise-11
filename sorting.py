import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(num_list):

    numbers = num_list.copy()

    for j in range(len(numbers)):

        min_index = j
        min_value = numbers[min_index]

        for i in range(j+1, len(numbers)):

            if numbers[i] < min_value:      # bude se provadet n**2 krat

                min_index = i
                min_value = numbers[i]

        numbers[j], numbers[min_index] = numbers[min_index], numbers[j]

    return numbers




if __name__ == "__main__":
    values = random_numbers(10)
    print(values)

    small = random_numbers(5, 0,20)
    print(small)

    select_sort = selection_sort(values)
    print(select_sort)