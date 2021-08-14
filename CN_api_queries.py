import datetime
import pprint
import requests 
from rich import print
import sys 


base_url = 'http://demo.codingnomads.co:8080/tasks_api'


def api_create_user() -> requests.Response:

    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email_address = input('Enter your email address: ')

    new_user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email_address
    }
    
    make_api_request = requests.post(base_url + '/users', new_user_info)

    if make_api_request.status_code == 200:
        print('[bold green] User created successfully! Find your user ID at the end[/bold green]\n')
    else:
            print('[warning] An error may have occurred, try again [/]')
            sys.exit()

    get_user_info = requests.get(base_url + '/users')
    display_user_info(get_user_info)    
    

def display_user_info(get_user_info) -> requests.Response:
    
    json_result = get_user_info.json()
    for user_id in json_result['data'][:-1]:
        test_id = user_id['id']
        print(test_id)


def api_view_all_tasks() -> requests.Response:

    userid = display_user_info.test_id
    delete_task(userid)
    try:
        tasks_info = {
            'userId': userid,
            'complete': 'all'
        }
        request_tasks = requests.get(base_url + '/tasks', json=tasks_info)
        print(f'Status: {request_tasks.status_code} \n')
        pprint.pprint(request_tasks.content)
        
    except Exception as err:
        print(err)


def view_completed_tasks() -> requests.Response:
    tasks_info = {
        'userId': api_view_all_tasks.userId,
        'complete': True
    } 

    complete_tasks = requests.get(base_url + '/tasks', json=tasks_info)
    print(f'Status: {complete_tasks.status_code} \n')
    pprint.pprint(complete_tasks.content)


def view_incomplete_tasks() -> requests.Response:
    tasks_info = {
        'userId': api_view_all_tasks.userId,
        'complete': False
    } 

    incomplete_tasks = requests.get(base_url + '/tasks', json=tasks_info)
    print(f'Status: {incomplete_tasks.status_code} \n')
    pprint.pprint(incomplete_tasks.content)


def create_new_task() -> requests.Response:
    task_desc = input('Enter a short task description: ')
    task_name = input('Enter a short task name: ')
    task_completion_info = datetime.datetime.now()
    
    task_body = {
        'completed': True,
        'createdAt': task_completion_info,
        'description': task_desc,
        'id': 0,
        'name': task_name,
        'updatedAt': task_completion_info,
        'userId': api_view_all_tasks.userId
    }

    new_task_request = requests.post(base_url + '/tasks', json=task_body)

    update_task(new_task_request)
    print(new_task_request.status_code)
    pprint.pprint(new_task_request.content)


def update_task(new_task_request) -> requests.Response:
    
    print(new_task_request.content)



def delete_task(userid) -> requests.Response:
    task_id = {
        'id': userid
    }

    delete_task_request = requests.delete(base_url + '/tasks', json=task_id)
    print(delete_task_request.status_code)
    pprint.pprint(delete_task_request)
