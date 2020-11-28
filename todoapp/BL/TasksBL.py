from ..DAL.TasksDAL import TasksDAL as ts
from ..DAL.CategoriesDAL import CategoriesDAL as ct
from ..Models.Task import Task

class TasksBL():

	def allTasks(icv):
		act = ts.allTasks(icv)
		Tasks = list()
		for i in act:
			tsk = Task()
			tsk.Id = i.t_id
			tsk.cateName = ct.selectOneCategoryI(i.cate_id).title
			tsk.title = i.title
			tsk.description = i.description
			tsk.dueDate = i.dueDate
			tsk.priority = i.priority
			tsk.isActive = i.isActive
			Tasks.append(tsk)
		return Tasks

	def addTask(ico):
		rcto = ts.addTask(ico)
		tsk = Task();
		tsk.Id = rcto.t_id
		return tsk

	def selectTask(ico):
		rcto = ts.selectOneTask(ico)
		tsk = Task();
		tsk.Id = rcto.t_id
		tsk.cateId = rcto.cate_id
		tsk.title = rcto.title
		tsk.description = rcto.description
		tsk.dueDate = rcto.dueDate
		tsk.priority = rcto.priority
		tsk.isActive = rcto.isActive
		return tsk

	def updateTask(ico):
		rcto = ts.updateTask(ico)
		tsk = Task();
		tsk.Id = rcto.t_id
		return tsk

	def deleteTask(ico):
		rcto = ts.deleteTask(ico)
		return rcto