import sys

if __name__ == "__main__":
    inventory = dict()
    for arg in sys.argv[1:]:
        colon_index = -1
        for i in range(len(arg)):
            if arg[i] == ':':
                colon_index = i
                break
        if colon_index != -1:
            key = arg[:colon_index]
            value = arg[colon_index + 1:]
            try:
                if key in inventory:
                    inventory[key] = inventory.get(key) + int(value)
                else:
                    inventory.update({key: int(value)})
            except ValueError:
                print(f"{value} is a bad value as an input!")

    print("=== Inventory System Analysis ===")
    total = 0
    for value in inventory.values():
        total = total + value
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")
    print()
    print("=== Current Inventory ===")
    sorted_inventory = dict()
    while len(sorted_inventory) < len(inventory):

        max = -1
        for key, value in inventory.items():

            if key not in sorted_inventory and value > max:
                max = value
                key_max = key
        sorted_inventory.update({key_max: max})

    for key, value in sorted_inventory.items():
        print(f"{key}: {value} units ({(value * (100 / total)):.1f}%)")

    Most_abundant = -1
    Least_abundant = 100
    print()
    print("=== Inventory Statistics ===")
    for key, value in inventory.items():
        if value > Most_abundant:
            Most_abundant = value
            name_max = key
        if value < Least_abundant:
            Least_abundant = value
            name_min = key

    print(f"Most abundant: {name_max} ({Most_abundant} units)")
    print(f"Least abundant: {name_min} ({Least_abundant} units)")

    print()
    print("=== Item Categories ===")
    moderate = dict()
    Scarce = dict()

    for key, value in inventory.items():
        if value >= 4:
            moderate.update({key: value})
        else:
            Scarce.update({key: value})

    print(f"Moderate: {moderate}")
    print(f"Scarce: {Scarce}")

    Restock_needed = dict()
    print()
    print("=== Management Suggestions ===")
    tmp = dict()
    print("Restock needed:", end=" ")
    for key, value in inventory.items():
        if value <= 1:
            tmp.update({key: value})
    string = ""
    checker = 0
    for key in tmp:
        string += key
        if checker < len(tmp) - 1:
            string += ", "
            checker += 1
    print(string)

    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    string = ""
    checker = 0
    for key, value in inventory.items():
        string = string + key
        if checker < len(inventory) - 1:
            string = string + ", "
            checker += 1
    print(string)
    print("Dictionary values:", end=" ")
    checker = 0
    for key, value in inventory.items():
        if checker < len(inventory) - 1:
            print(value, end=', ')
        else:
            print(value)
        checker += 1
    key = "sword"
    if key in inventory:
        print(f"Sample lookup - '{key}' in inventory: True")
