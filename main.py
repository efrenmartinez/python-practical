# -*-  coding: utf8 -*-


clients = 'Efren,Hector,'


def create_client(client_name):
	"""Create new client."""
	global clients
	
	if name_client not in clients:
		clients += client_name
		_add_comma()
	else:
		print('The name already is in client´s list.')


def update_client(client_name, updated_name_client):
	"""Update client"""
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', updated_name_client + ',')
	else:
		print('Client not found.')


def delete_client(client_name):
	"""Delete client"""
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		print('Client not found.')


def _add_comma(): #función privada
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


def _get_client_name():
	return input('What´s is name client? ').capitalize()


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
		name_client = _get_client_name()
		updated_name_client = input('What´s new name client? ').capitalize()
		update_client(name_client, updated_name_client)
		list_client()

	elif command == 'D':
		name_client = _get_client_name()
		confirm_delete = input('You want to delete the client?  y/n ').lower()
		if confirm_delete == 'y':
			delete_client(name_client)
			list_client()
		else:
			pass

	else:
		print('Invalid command')
