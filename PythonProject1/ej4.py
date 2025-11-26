#this creates the files
from pathlib import Path
def setup_environment():
    base = Path("Recetas")

    # Define the structure based on the image in the PDF
    structure = {
        "Carnes": ["Entrecot al Malbec.txt", "Matambre a la Pizza.txt"],
        "Ensaladas": ["Ensalada Griega.txt", "Ensalada Mediterranea.txt"],
        "Pastas": ["Canelones de Espinaca.txt", "Ravioles de Ricotta.txt"],
        "Postres": ["Compota de Manzana.txt", "Tarta de Frambuesa.txt"]
    }

    # Create directories and dummy files
    if not base.exists():
        base.mkdir()

    for category, recipes in structure.items():
        cat_path = base / category
        cat_path.mkdir(exist_ok=True)
        for recipe in recipes:
            file_path = cat_path / recipe
            if not file_path.exists():
                file_path.write_text(f"Instructions for {recipe}...")

    print(f"Environment created at: {base.resolve()}")


if __name__ == "__main__":
    setup_environment()
#this is the program
import os
from pathlib import Path
import shutil

base_path = Path("Recetas")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def count_recipes(path):
    count = 0
    for txt_file in path.glob("**/*.txt"):
        count += 1
    return count


def get_categories(path):
    """Returns a list of category folders."""
    return [x for x in path.iterdir() if x.is_dir()]


def get_recipes_in_category(category_path):
    """Returns a list of .txt files in a specific category."""
    return [x for x in category_path.glob("*.txt")]


def choose_category():
    """Helper to let user pick a category."""
    categories = get_categories(base_path)
    print("\nSelect a category:")
    for i, cat in enumerate(categories):
        print(f"{i + 1}. {cat.name}")

    try:
        choice = int(input("\nChoice number: ")) - 1
        if 0 <= choice < len(categories):
            return categories[choice]
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input.")
        return None


def read_recipe():
    """Option 1: Read a recipe."""
    category = choose_category()
    if category:
        recipes = get_recipes_in_category(category)
        if not recipes:
            print("No recipes found in this category.")
            return

        print(f"\nRecipes in {category.name}:")
        for i, recipe in enumerate(recipes):
            print(f"{i + 1}. {recipe.stem}")

        try:
            choice = int(input("\nChoose a recipe to read: ")) - 1
            if 0 <= choice < len(recipes):
                content = recipes[choice].read_text()
                print(f"\n--- {recipes[choice].stem} ---")
                print(content)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")


def create_recipe():
    """Option 2: Create a recipe."""
    category = choose_category()
    if category:
        name = input("Enter the name of the new recipe: ") + ".txt"
        content = input("Write the content of the recipe:\n")
        new_file = category / name
        new_file.write_text(content)
        print(f"Recipe '{name}' created successfully!")


def create_category():
    """Option 3: Create a category."""
    name = input("Enter the name of the new category: ")
    new_dir = base_path / name
    if not new_dir.exists():
        new_dir.mkdir()
        print(f"Category '{name}' created successfully!")
    else:
        print("That category already exists.")


def delete_recipe():
    """Option 4: Delete a recipe."""
    category = choose_category()
    if category:
        recipes = get_recipes_in_category(category)
        print(f"\nRecipes in {category.name}:")
        for i, recipe in enumerate(recipes):
            print(f"{i + 1}. {recipe.stem}")

        try:
            choice = int(input("\nChoose a recipe to DELETE: ")) - 1
            if 0 <= choice < len(recipes):
                recipes[choice].unlink()
                print("Recipe deleted.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")


def delete_category():
    """Option 5: Delete a category."""
    category = choose_category()
    if category:
        shutil.rmtree(category)
        print(f"Category '{category.name}' deleted.")


def main():
    if not base_path.exists():
        print(f"Error: Directory '{base_path}' not found. Please run the setup script first.")
        return

    while True:
        print("-" * 40)
        print("     RECIPE MANAGER     ")
        print("-" * 40)
        print(f"Recipes location: {base_path.resolve()}")
        print(f"Total recipes: {count_recipes(base_path)}\n")

        print("[1] - Read Recipe")
        print("[2] - Create Recipe")
        print("[3] - Create Category")
        print("[4] - Delete Recipe")
        print("[5] - Delete Category")
        print("[6] - End Program")

        option = input("\nChoose an option: ")

        if option == '1':
            read_recipe()
        elif option == '2':
            create_recipe()
        elif option == '3':
            create_category()
        elif option == '4':
            delete_recipe()
        elif option == '5':
            delete_category()
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
        input("\nPress Enter to return to the menu...")
        clear_console()


if __name__ == "__main__":
    main()