from ..Entities.Categories import Categories as ct
import datetime
from django.db.models import Q

class CategoriesDAL:
	def allCategories(icv):
		return ct.objects.filter(user_id=icv).all()
	def addCategory(ico):
		return ct.objects.create(title=ico.title, user_id=ico.user_id, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneCategory(ico):
		return ct.objects.get(c_id=ico.Id, user_id=ico.user_id)
	def selectOneCategoryI(icv):
		return ct.objects.get(c_id=icv)
	def updateCategory(ico):
		qrr = ct.objects.filter(c_id=ico.Id, user_id=ico.user_id).update(title=ico.title, user_id=ico.user_id, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, ct.objects.get(c_id=ico.Id)) [qrr != 0]
	def deleteCategory(ico):
		qrr = ct.objects.filter(c_id=ico.Id, user_id=ico.user_id).delete()
		return (False, True) [qrr[0] != 0]