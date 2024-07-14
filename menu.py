import library
from colorama import Fore
def display_menu():
    print(f"{Fore.MAGENTA}L{Fore.GREEN}I{Fore.RED}B{Fore.CYAN}R{Fore.BLUE}A{Fore.YELLOW}R{Fore.MAGENTA}Y {Fore.MAGENTA}M{Fore.GREEN}A{Fore.RED}N{Fore.CYAN}A{Fore.BLUE}G{Fore.YELLOW}E{Fore.MAGENTA}M{Fore.RED}E{Fore.GREEN}N{Fore.CYAN}T {Fore.RED}S{Fore.CYAN}Y{Fore.BLUE}S{Fore.YELLOW}T{Fore.MAGENTA}E{Fore.RED}M")
    print(Fore.MAGENTA + "1. Add Book")
    print(Fore.GREEN + "2. View All Books")
    print(Fore.CYAN + "3. Search Books")
    print(Fore.BLUE + "4. Search Books by Author")
    print(Fore.YELLOW + "5. Remove Book")
    print(Fore.MAGENTA + "6. Lend Book")
    print(Fore.GREEN + "7. Return Book")
    print(Fore.RED+ "8. View Lent Books")
    print(Fore.CYAN +"9. Exit")
    print(Fore.RED + """ 
    ___  ___    ___
  / ___| | |    | |
 | |     | |    | |
 | |___  | |___ | |
  \____| |_|___||_|
         """)

def handle_menu(library_instance):
    while True:
        display_menu()
        choice = input(Fore.MAGENTA + "Enter your choice: ")
        if choice == '1':
            title = input(Fore.GREEN+"Enter title: ")
            authors = input(Fore.RED +"Enter authors (comma-separated): ").split(',')
            isbn = input(Fore.BLUE +"Enter ISBN: ")
            year = input(Fore.CYAN +"Enter publishing year: ")
            price = float(input(Fore.YELLOW+"Enter price: "))
            quantity = int(input(Fore.CYAN +"Enter quantity: "))
            print(Fore.GREEN + "Book created successfullu!!")
            library_instance.add_book(title, authors, isbn, year, price, quantity)
        elif choice == '2':
            library_instance.view_books()
        elif choice == '3':
            term = input(Fore.MAGENTA +"Enter search term (title or ISBN): ")
            library_instance.search_books(term)
        elif choice == '4':
            author = input(Fore.GREEN +"Enter author name: ")
            library_instance.search_books_by_author(author)
        elif choice == '5':
            term = input(Fore.RED +"Enter title or ISBN of book to remove: ")
            library_instance.remove_book(term)
        elif choice == '6':
            term = input(Fore.MAGENTA +"Enter title or ISBN of book to lend: ")
            lent_to = input(Fore.CYAN +"Enter name of person lending to: ")
            library_instance.lend_book(term, lent_to)
        elif choice == '7':
            term = input(Fore.YELLOW +"Enter title or ISBN of book to return: ")
            library_instance.return_book(term)
        elif choice == '8':
            library_instance.view_lent_books()
        elif choice == '9':
            print(Fore.MAGENTA +"Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

