from ..Entities.Users import Users as u
from .Commons import Commons as c
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class UsersDAL:
	def allUsers():
		return u.objects.all()
	def getLatestUser():
		uo = None
		try:
			uo = u.objects.latest('u_id')
		except ObjectDoesNotExist:
		 	uo = None
		return uo
	def addUser(ico):
		unq_id = c.getUniqueId(UsersDAL.getLatestUser())
		return u.objects.create(unq_id=unq_id, contact_id=ico.contact_id, username=ico.username, emailAddr=ico.emailAddr, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def updateToken(ico):
		qrr = u.objects.filter(unq_id=ico.Id).update(auth_token=ico.auth_token, token_expiry=ico.token_expiry)
		return (None, u.objects.get(unq_id=ico.Id)) [qrr != 0]
	def selectUserbyUsernameOrEmail(ico):
		try:
			return u.objects.filter(Q(emailAddr=ico.emailAddr) | Q(username=ico.username))[0]
		except IndexError:
			return None