def calculate_average(numbers):
    total = sum(numbers)
    try:
     return total / len(numbers)
    except ZeroDivisionError:
        print("No numbers in the list")
        return 0

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers] #agora aceita numeros com ponto flutuante
    return numbers

def main():
    numbers = get_numbers()
    print(f"Average: ", calculate_average(numbers))
    try:
        print("Maximum:", find_max(numbers))
    except IndexError:
        print("Empty List")
if __name__ == "__main__":
    main()