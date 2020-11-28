from ..DAL.PasswordsDAL import PasswordsDAL as pd
from ..Models.Password import Password

class PasswordsBL():

	def allPasswords():
		apd = pd.allPasswords()
		Passwords = list()
		for i in apd:
			Psswrd = Password()
			Psswrd.Id = i.p_id
			Psswrd.user_id = i.user_id
			Psswrd.password = i.password
			Psswrd.isActive = i.isActive
			Passwords.append(Psswrd)
		return Passwords

	def addPassword(ico):
		rpo = pd.addPassword(ico)
		Psswrd = Password()
		Psswrd.Id = rpo.p_id
		Psswrd.user_id = rpo.user_id
		Psswrd.password = rpo.password
		Psswrd.isActive = rpo.isActive
		return Psswrd

	def selectPassword(ico):
		rpo = pd.selectOnePassword(ico)
		Psswrd = Password()
		Psswrd.Id = rpo.p_id
		Psswrd.user_id = rpo.user_id
		Psswrd.password = rpo.password
		Psswrd.isActive = rpo.isActive
		return Psswrd

	def selectUserPassword(ico):
		rpo = pd.selectUserPassword(ico)
		if(rpo is None):
			return None
		Psswrd = Password()
		Psswrd.Id = rpo.p_id
		Psswrd.user_id = rpo.user_id
		Psswrd.password = rpo.password
		Psswrd.isActive = rpo.isActive
		return Psswrd

	def updatePassword(ico):
		rpo = pd.updatePassword(ico)
		Psswrd = Password()
		Psswrd.Id = rpo.p_id
		Psswrd.user_id = rpo.user_id
		Psswrd.password = rpo.password
		Psswrd.isActive = rpo.isActive
		return Psswrd

	def deletePassword(ico):
		rpo = pd.deletePassword(ico)
		return rpo