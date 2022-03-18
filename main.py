from simple_term_menu import TerminalMenu

main_menu = ["[1]   Youtube Scrapper", "[2]     Instagram Scrapper", "[q] quit"]
sub_menu = ["[1] Youtube Scraper Comment", "[2] Analysis", "[c] go back"]
sub_menu1 =["[1] Instagram All Post Scrapper", "[2] Instagram Link Post Scrapper", "[3] Instagram Scraper with Userlist", "[4] Analysis", "[c] go back"]

loop = True

while loop:
    choice = main_menu[TerminalMenu(main_menu, title = "Main menu", menu_cursor_style = ("fg_green", "bold"), menu_highlight_style = ("fg_black", "bg_green"), menu_cursor = "~").show()]

    if choice == "[1]   Youtube Scrapper":
        sub_loop = True
        while sub_loop:
            choice = sub_menu[TerminalMenu(sub_menu, title = "Youtube Menu").show()]

            if choice == "[1] Youtube Scraper Comment":
                exec(open("youtube.py").read())

            elif choice == "[2] Analysis":
                exec(open("analisis.py").read())

            elif choice == "[c] go back":
                sub_loop = False

    elif choice == "[2]     Instagram Scrapper":
        sub_loop = True
        while sub_loop:
            choice = sub_menu1[TerminalMenu(sub_menu1, title = "Instagram Menu").show()]

            if choice == "[1] Instagram All Post Scrapper":
                exec(open("ig-user-scraper.py").read())

            elif choice == "[2] Instagram Link Post Scrapper":
                exec(open("ig-post-scraper.py").read())

            elif choice == "[3] Instagram Scraper with Userlist":
                exec(open("ig-list-scraper.py").read())

            elif choice == "[4] Analysis":
                exec(open("analisis.py").read())

            elif choice == "[c] go back":
                sub_loop = False

    elif choice == "[q] quit":
        loop = False