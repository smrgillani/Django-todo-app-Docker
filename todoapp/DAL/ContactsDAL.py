from ..Entities.Contacts import Contacts as c
import datetime

class ContactsDAL:
	def allContacts():
		return c.objects.all()
	def addContact(ico):
		return c.objects.create(salutation=ico.salutation, firstName=ico.firstName, middleName=ico.middleName, lastName=ico.lastName, dob=ico.dob, mobileNumber=ico.mobileNumber, image=ico.image, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneContact(ico):
		return c.objects.get(id=ico.Id)
	def selectUserContact(contact_id):
		return c.objects.get(id=contact_id)