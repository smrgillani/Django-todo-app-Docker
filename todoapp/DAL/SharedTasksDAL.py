from ..Entities.SharedTasks import SharedTasks as st
import datetime
from django.core.exceptions import ObjectDoesNotExist

class SharedTasksDAL:
	def allSharedTasks(icv):
		return st.objects.filter(user_id=icv).all()
	def addSharedTask(ico):
		return st.objects.create(user_id=ico.userId, task_id=ico.taskId, created_at=datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S.%f"))
	def selectOneSharedTask(ico):
		uo = None
		try:
			uo = st.objects.get(user_id=ico.userId, task_id=ico.taskId)
		except ObjectDoesNotExist:
		 	uo = None
		return uo
	def deleteSharedTask(ico):
		qrr = st.objects.filter(st_id=ico.Id, user_id=ico.userId).delete()
		return (False, True) [qrr[0] != 0]