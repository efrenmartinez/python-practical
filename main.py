# -*-  coding: utf8 -*-


clients = 'Hola,mundo,'


def create_client(client_name):
	global clients
	
	if name_client not in clients:
		clients += client_name
		_add_comma()
	else:
		print('The name already is in client´s list.')


def _add_comma(): #función privada
	global clients
	clients += ','


def list_client():
	global clients
	print(clients)


def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 20)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[D]elete client')


if __name__ == '__main__':
	_print_welcome()

	command = input('Please tell us your option: ').upper()

	if command == 'C':
		name_client = input('Name client: ')
		create_client(name_client)
		list_client()
	elif command == 'D':
		pass
	else:
		print('Invalid command')

