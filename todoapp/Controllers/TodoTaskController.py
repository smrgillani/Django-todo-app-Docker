from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template import loader

from ..BL.UsersBL import UsersBL as ubl
from ..BL.TasksBL import TasksBL as tbl
from ..BL.SharedTasksBL import SharedTasksBL as stbl
from ..BL.CategoriesBL import CategoriesBL as cbl
from ..Models import *
import json
class TodoTaskController:

	@method_decorator(login_required)
	def addUpdateTask(self, request, task_id=None):
		formMsg = ""
		to = Task.Task();

		if request.method == 'POST':
			formMsg = self.checkMissingFormKey(request)
			if(len(formMsg) == 0):

				uco = Task.Task();
				uco.Id = request.POST.get('taskId',0)
				uco.user_id = request.user.get_userUnqId()
				uco.cateId = request.POST['categories']
				uco.title = request.POST['title']
				uco.description = request.POST['description']
				uco.dueDate = request.POST['dueDate']
				uco.priority = request.POST['priority']
				uco.isActive = request.POST.get('isActive','off')
				if uco.Id != '0':
					print(uco.Id)
					print("updating")
					uco = tbl.updateTask(uco)
				else:
					print("adding")
					uco = tbl.addTask(uco)
				return redirect('/')
		else:
			if task_id is not None:
				to.Id = task_id
				to.user_id = request.user.get_userUnqId()
				to = tbl.selectTask(to)

		return render(request, 'task.html', {'formMsg': formMsg, 'taskObj': to, 'records': cbl.allCategories(request.user.get_userUnqId())})

	@method_decorator(login_required)
	def removeTask(self, request, task_id=None):
		if task_id is not None:
			co = Task.Task();
			co.Id = task_id
			co.user_id = request.user.get_userUnqId()
			tbl.deleteTask(co)
		return redirect('/')

	@method_decorator(login_required)
	def shareTask(self, request):
		formMsg = ""
		if request.method == 'POST':
			ud = json.loads(request.body)
			udo = User.User()
			udo.emailAddr = ud['emailAddr']
			udo = ubl.selectUserbyUsernameOrEmail(udo)
			if(udo is not None):
				if(udo.Id != request.user.get_userUnqId()):
					sto = SharedTask.SharedTask()
					sto.userId = udo.Id
					sto.taskId = ud['taskId']
					_stbl = stbl.selectSharedTask(sto)
					if(_stbl is None):
						stbl.addSharedTask(sto)
						formMsg = {'success':"Task has been shared"}
					else:
						formMsg = {'error':"You are trying to add duplicate entry"}
				else:
					formMsg = {'error':"Please don't enter your own email or username"}
			else:
				formMsg = {'error':'User Not Found'}
			#sto = shareTask.shareTask();
			#uupo.userRole_id = ud['taskid']
		return HttpResponse(Common.Common().ConverttoJson(formMsg), content_type="application/json")

	def checkMissingFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['categories'] = "Category "
		dataDict['title'] = "Title "
		dataDict['description'] = "Description "
		dataDict['dueDate'] = "Due Date "
		dataDict['priority'] = "Priority "
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr