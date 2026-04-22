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


import matplotlib.pyplot as plt

def bubble_sort(num_list):

    numbers = num_list.copy()

    plt.ion()
    plt.show()

    for j in range(len(numbers)):

        swapped = False

        for i in range(0, len(numbers)-j-1):

            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if numbers[i] > numbers[i+1]:

                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

                swapped = True

        if not swapped:

            plt.ioff()
            plt.show()

            return numbers

    plt.ioff()
    plt.show()

    return numbers


if __name__ == "__main__":
    values = random_numbers(20)
    print(values)

    small = random_numbers(5, 0,20)
    print(small)

    select_sort = selection_sort(values)
    print(select_sort)

    bubble = bubble_sort(values)
    print(bubble)