shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    def add_item():
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")

    def remove_item():
        item = input("Enter item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' not found in the list.")

    def view_list():
        if shopping_list:
            print("\nCurrent Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("\nYour shopping list is empty.")