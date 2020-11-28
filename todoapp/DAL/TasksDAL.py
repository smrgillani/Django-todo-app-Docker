from ..Entities.Tasks import Tasks as ts
import datetime
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

class TasksDAL:
	def allTasks(icv):
		return ts.objects.filter(user_id=icv).all()
	def addTask(ico):
		return ts.objects.create(user_id=ico.user_id, cate_id=ico.cateId, title=ico.title, description=ico.description, dueDate=ico.dueDate, priority=ico.priority, isActive=ico.isActive, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneTask(ico):
		return ts.objects.get(t_id=ico.Id, user_id=ico.user_id)
	def selectOneTaskI(icv):
		uo = None
		try:
			uo = ts.objects.get(t_id=icv)
		except ObjectDoesNotExist:
		 	uo = None
		return uo
	def updateTask(ico):
		qrr = ts.objects.filter(t_id=ico.Id, user_id=ico.user_id).update(cate_id=ico.cateId, title=ico.title, description=ico.description, dueDate=ico.dueDate, priority=ico.priority, isActive=ico.isActive, updated_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
		return (None, ts.objects.get(t_id=ico.Id)) [qrr != 0]
	def deleteTask(ico):
		qrr = ts.objects.filter(t_id=ico.Id, user_id=ico.user_id).delete()
		return (False, True) [qrr[0] != 0]