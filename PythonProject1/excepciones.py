def main():
    shopping_list = []

    while True:
        print("\n=== Shopping List ===")
        print("1. Add product")
        print("2. Remove product")
        print("3. Show list")
        print("4. Exit")

        try:
            option = input("Choose an option: ")

            if option == '1':
                product = input("Product: ")



                shopping_list.append(product)
                print(f"'{product}' added.")

            elif option == '2':

                print("\n--- Current List ---")
                for index, item in enumerate(shopping_list):
                    print(f"{index}: {item}")

                idx_input = input("Position to remove: ")

                idx = int(idx_input)

                removed_item = shopping_list.pop(idx)
                print(f"Removed '{removed_item}'")

            elif option == '3':
                print("\n--- Complete Shopping List ---")
                if not shopping_list:
                    print("(List is empty)")
                else:
                    for item in shopping_list:
                        print(f"- {item}")

            elif option == '4':
                print("Exiting program...")
                break

            else:
                raise Exception("Invalid menu option selected")

        except ValueError as e:
            print(f"Error: {e}")

        except IndexError:
            # Catches indices that do not exist 
            print("Error: index out of range")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            print("Operation completed")


if __name__ == "__main__":
    main()