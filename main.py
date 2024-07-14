from library import Library
from menu import handle_menu

def main():
    library_instance = Library()
    handle_menu(library_instance)

if __name__ == "__main__":
    main()
