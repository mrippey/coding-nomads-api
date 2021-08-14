import CN_api_queries

from rich import print
import sys


def show_menu() -> None:
    print()
    print('Author: Michael Rippey\n')
    print('Select one item from the menu below: \n')
    print('[magenta] 1 [/]' +  '[yellow]Create a new user [/]' + '[white] POST [/]')
    print('[magenta] 2 [/]' +  '[yellow]View all tasks' + '[white] GET [/]')
    print('[magenta] 3 [/]' +  '[yellow]View completed tasks' + '[white] GET [/]')
    print('[magenta] 4 [/]' +  '[yellow]View only incomplete tasks [/]' + ' [white] GET [/]')
    print('[magenta] 5 [/]' +  '[yellow]Create a new task [/]' + '[white] POST [/]')
    print('[magenta] 6 [/]' +  '[yellow]Update exisiting task [/]' + '[white] PATCH/PUT [/]')
    print('[magenta] 7 [/]' +  '[yellow]Delete a task [/]' + '[white] DELETE [/]')
    print('[bold red] Q [/]' +  '[bold red] Quit Program [/]' )


def main():

    while True:
        show_menu()
        print('\n')
        menu_choice = input('[MENU] ' + ' Enter a selection from the choices above:  ' )
        print('\n')

        if menu_choice.lower() == 'q':
            sys.exit() 

        elif menu_choice.lower() == '1':
            CN_api_queries.api_create_user()
        
        elif menu_choice.lower() == '2':
            CN_api_queries.api_view_all_tasks()

        elif menu_choice.lower() == '3':
            CN_api_queries.view_completed_tasks()

        elif menu_choice.lower() == '4':
            CN_api_queries.view_incomplete_tasks()

        elif menu_choice.lower() == '5':
            CN_api_queries.create_new_task()

        elif menu_choice.lower() == '6':
            CN_api_queries.update_task()

        elif menu_choice.lower() == '7':
            CN_api_queries.delete_task() 


if __name__ == '__main__':
    main()
