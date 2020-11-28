from ..Entities.Passwords import Passwords as p
from django.db.models import Q
import datetime

class PasswordsDAL:
	def allPasswords():
		return p.objects.all()
	def addPassword(ico):
		return p.objects.create(user_id=ico.user_id, password=ico.password, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOnePassword(ico):
		return p.objects.get(p_id=ico.Id)
	def selectUserPassword(ico):
		try:
			pswd = p.objects.get(Q(user_id=ico.user_id) & Q(password=ico.password))
		except p.DoesNotExist:
			return None
		return pswd if pswd is not None else None
	def updatePassword(ico):
		qrr = p.objects.filter(p_id=ico.Id).update(user_id=ico.user_id, password=ico.password, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, p.objects.get(p_id=ico.Id)) [qrr != 0]
	def deletePassword(ico):
		qrr = p.objects.filter(p_id=ico.Id).delete()
		return (False, True) [qrr[0] != 0]