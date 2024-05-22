def calculate_flame_count(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    count = 0
    for char in name1:
        if char in name2:
            name2 = name2.replace(char, "", 1)
        else:
            count += 1
    return count + len(name2)

def get_flame_result(count):
    flames = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    return flames[(count - 1) % len(flames)]

def main():
    print("Welcome to the FLAME game!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    count = calculate_flame_count(name1, name2)
    result = get_flame_result(count)
    print(f"The FLAME result between {name1} and {name2} is: {result}")

if __name__ == "__main__":
    main()
