from ..DAL.SharedTasksDAL import SharedTasksDAL as st
from ..DAL.TasksDAL import TasksDAL as t
from ..Models.SharedTask import SharedTask
from ..Models.Task import Task
from ..DAL.CategoriesDAL import CategoriesDAL as ct

class SharedTasksBL():

	def allSharedTasks(icv):
		act = st.allSharedTasks(icv)
		Tasks = list()
		for i in act:
			ste = t.selectOneTaskI(i.task_id)
			if ste is not None:
				tsk = Task()
				tsk.Id = ste.t_id
				tsk.cateName = ct.selectOneCategoryI(ste.cate_id).title
				tsk.title = ste.title
				tsk.description = ste.description
				tsk.dueDate = ste.dueDate
				tsk.priority = ste.priority
				tsk.isActive = ste.isActive
				Tasks.append(tsk)
		return Tasks

	def addSharedTask(ico):
		rcto = st.addSharedTask(ico)
		stsk = SharedTask();
		stsk.Id = rcto.st_id
		return stsk

	def selectSharedTask(ico):
		rcto = st.selectOneSharedTask(ico)
		if rcto is None:
			return None
		stsk = SharedTask();
		stsk.Id = rcto.st_id
		stsk.userId = rcto.user_id
		stsk.taskId = rcto.task_id
		return stsk

	# def updateCategory(ico):
	# 	rcto = st.updateCategory(ico)
	# 	stsk = Category();
	# 	stsk.Id = rcto.c_id
	# 	return stsk

	# def deleteCategory(ico):
	# 	rcto = st.deleteCategory(ico)
	# 	return rcto