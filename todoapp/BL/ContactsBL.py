from ..DAL.ContactsDAL import ContactsDAL as cd
from ..Models.Contact import Contact

class ContactsBL():

	def allContacts():
		ac = cd.allContacts()
		Contacts = list()
		for i in ac:
			cntct = Contact()
			cntct.salutation = i.salutation
			cntct.firstName = i.firstName
			cntct.middleName = i.middleName
			cntct.lastName = i.lastName
			cntct.dob = i.dob
			cntct.mobileNumber = i.mobileNumber
			cntct.image = i.image
			cntct.isActive = i.isActive
			cntct.created_at = i.created_at
			Contacts.append(cntct)
		return Contacts

	def addContact(ico):
		Contct = Contact()
		Cntct = cd.addContact(ico);
		Contct.id = Cntct.id
		Contct.salutation = Cntct.salutation
		Contct.firstName = Cntct.firstName
		Contct.middleName = Cntct.middleName
		Contct.lastName = Cntct.lastName
		Contct.dob = Cntct.dob
		Contct.mobileNumber = Cntct.mobileNumber
		Contct.image = Cntct.image
		Contct.isActive = Cntct.isActive
		return Contct

	def selectContact(ico):
		Contct = Contact()
		Cntct = cd.selectOneContact(ico);
		Contct.id = Cntct.id
		Contct.salutation = Cntct.salutation
		Contct.firstName = Cntct.firstName
		Contct.middleName = Cntct.middleName
		Contct.lastName = Cntct.lastName
		Contct.dob = Cntct.dob
		Contct.mobileNumber = Cntct.mobileNumber
		Contct.image = Cntct.image
		Contct.isActive = Cntct.isActive
		return Contct