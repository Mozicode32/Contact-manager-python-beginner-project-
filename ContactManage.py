class ContactManagerPro:
	def __init__(self):
		self.contact_list={}

	def add_contact(self):
		name=input('enter name: ').lower()
		number=input('enter number: ')
		email=input('enter email: ').lower()
		if name not in self.contact_list:
			self.contact_list[name]=number,email
			print('contact saved successfully!!!')
		else:
			print('that name is already in the contact')
			
	def display_contact(self):
		for name,distails in self.contact_list.items():
			number,email=distails
			print(f'{name} - number = {number} - email = {email}')
			
	def search_contact(self):
		search=input('search🔎: ').lower()
		if search in self.contact_list.keys():
			print(f'{search} - {self.contact_list[search]}')
		else:
			print('not in contact')
			
	def edit_contact(self):
		contact=input('what contact do you want to edit: ').lower()
		if contact in self.contact_list.keys():
			edit_name=input('enter new name: ').lower()
			edit_no=input('enter new number: ')
			edit_email=input('enter new email: ').lower()
			if edit_name not in self.contact_list or edit_name == contact:
				self.contact_list[edit_name]=edit_no,edit_email
				self.contact_list.pop(contact,None)
				print(f'{edit_name} - {self.contact_list[edit_name]}')
			else:
				print('the name already exist')
		else:
			print('''you can't edit what is not in your contact''')
			
	def delete_contact(self):
		contact_to_delete=input('enter contact you want to delete: ').lower()
		if contact_to_delete in self.contact_list.keys():
			self.contact_list.pop(contact_to_delete,None)
			print(f'you have successfully deleted {contact_to_delete}')
			
			
contact=ContactManagerPro()
while True:
	print('''====CONTACT MANAGER====
	   1. add contact
	   2. display contact
	   3. search contact
	   4. edit contact
	   5. delete contact 
	   6. exit''')
	choose=int(input('choose an option: '))
	match choose:
		case 1:
			contact.add_contact()
		case 2:
			contact.display_contact()
		case 3:
			contact.search_contact()
		case 4:
			contact.edit_contact()
		case 5:
			contact.delete_contact()
		case 6:
			break
		case _:
			print('invalid option')
