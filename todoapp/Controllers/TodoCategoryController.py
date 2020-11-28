from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template import loader

from ..BL.CategoriesBL import CategoriesBL as cbl
from ..Models import *
import json
class TodoCategoryController:

	@method_decorator(login_required)
	def addUpdateCategory(self, request, cate_id=None):
		formMsg = ""
		co = Category.Category();

		if request.method == 'POST':
			formMsg = self.checkMissingFormKey(request)
			if(len(formMsg) == 0):

				uco = Category.Category();
				uco.Id = request.POST.get('catId',0)
				uco.user_id = request.user.get_userUnqId()
				uco.title = request.POST['title']
				uco.isActive = request.POST.get('isActive','off')
				if uco.Id != 0:
					uco = cbl.updateCategory(uco)
				else:
					uco = cbl.addCategory(uco)
				return redirect('/categories')
		else:
			if cate_id is not None:
				co.Id = cate_id
				co.user_id = request.user.get_userUnqId()
				co = cbl.selectCategory(co)

		return render(request, 'category.html', {'formMsg': formMsg, 'catObj': co})

	@method_decorator(login_required)
	def removeCategory(self, request, cate_id=None):
		if cate_id is not None:
			co = Category.Category();
			co.Id = cate_id
			co.user_id = request.user.get_userUnqId()
			cbl.deleteCategory(co)
		return redirect('/categories')

	@method_decorator(login_required)
	def allCategories(self, request):
		return render(request, 'categories.html', {'records': cbl.allCategories(request.user.get_userUnqId())})

	def checkMissingFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['title'] = "Title "
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr