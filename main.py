# -*-  coding: utf8 -*-

import sys

clients = ['Juan']


def create_client(client_name):
    """Create new client."""
    global clients

    if name_client not in clients:
        clients.append(client_name)
    else:
        print('The name already is in client´s list.')


def update_client(client_name, updated_name_client):
    """Update client"""
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name_client
    else:
        print('Client not found.')


def delete_client(client_name):
    """Delete client"""
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client not found.')


def search_client(client_name):
    """Search client"""
    global clients

    client_list = clients.split(',')
    for client in client_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma():  # función privada
    """Add a comma at the end"""
    global clients
    clients += ','


def list_client():
    """List client."""
    global clients
    print(clients)


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 20)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[E]xit')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What´s is name client? ').capitalize()

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input('Please tell us your option: ').upper()

    if command == 'C':
        name_client = _get_client_name()
        create_client(name_client)
        list_client()

    elif command == 'R':
        list_client()

    elif command == 'U':
        list_client()
        name_client = _get_client_name()
        updated_name_client = input('What´s new name client? ').capitalize()
        update_client(name_client, updated_name_client)
        list_client()

    elif command == 'D':
        list_client()
        name_client = _get_client_name()
        confirm_delete = input('You want to delete the client?  y/n ').lower()
        if confirm_delete == 'y':
            delete_client(name_client)
            list_client()
        else:
            pass

    elif command == 'S':
        name_client = _get_client_name()
        found = search_client(name_client)

        if found:
            print('The client is in the client´s list.')
        else:
            print('The client: {} is not client´s list'.format(name_client))

    elif command == 'E':
        sys.exit()

    else:
        print('Invalid command')
