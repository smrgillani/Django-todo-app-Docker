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
from ..BL.ContactsBL import ContactsBL as cbl
from ..BL.PasswordsBL import PasswordsBL as pbl
from ..Models import *
import json
class UserController:
	def userSignup(self, request):
		formMsg = ""
		if request.method == 'POST':
			formMsg = self.checkMissingRegisterFormKey(request)
			if(len(formMsg) == 0):

				if(request.POST['password'] == request.POST['pswRepeat']):
					udo = User.User()
					udo.username = request.POST['username']
					udo.emailAddr = request.POST['emailAddr']
					if(ubl.selectUserbyUsernameOrEmail(udo) is None):
						uco = Contact.Contact();
						uco.salutation = request.POST['salutation']
						uco.firstName = request.POST['firstName']
						uco.middleName = request.POST['middleName']
						uco.lastName = request.POST['lastName']
						uco.mobileNumber = request.POST['mobileNumber']
						uco.dob = request.POST['birthDate']
						uco.isActive = True
						
						uco = cbl.addContact(uco)
						
						udo.contact_id = uco.id

						udo = ubl.addUser(udo)

						upo = Password.Password();
						upo.user_id = udo.Id
						upo.password = request.POST['password']
						upo.isActive = True
						pbl.addPassword(upo)
						return redirect('/login')
					else:
						formMsg = "User Already Exists with the same Username Or Email !"
				else:
					formMsg = "Password didn't match with Repeat Password !"

		return render(request, 'register.html', {'formMsg': formMsg})

	def userLoginRd(self, request):
		return redirect('/login')

	def userLogin(self, request):
		formMsg = ""
		if request.method == 'POST':
			formMsg = self.checkMissingLoginFormKey(request)
			if(len(formMsg) == 0):
				usernameOrEmail = request.POST['usernameOrEmail']
				upo = Password.Password();
				upo.password = request.POST['password']
				user = authenticate(request, username=usernameOrEmail)
				if user is not None:
					upo.user_id = user.get_userUnqId()
					gup = pbl.selectUserPassword(upo)
					if gup is not None:
						login(request, user)
						print(request.user.u_id)
						return redirect('/')
					else:
						formMsg = "Password is incorrect !"
				else:
					formMsg = "Username or Email not found !"
		return render(request, 'login.html', {'formMsg': formMsg, 'request':request})

	@method_decorator(login_required)
	def userDashboard(self, request):
		return render(request, 'index.html', {'records': tbl.allTasks(request.user.get_userUnqId()), 'precords': stbl.allSharedTasks(request.user.get_userUnqId())})

	@method_decorator(login_required)
	def userLogout(self, request):
		logout(request)
		return redirect('/')

	def checkMissingRegisterFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['salutation'] = "Salutation"
		dataDict['firstName'] = "First Name"
		dataDict['middleName'] = "Middle Name"
		dataDict['lastName'] = "Last Name"
		dataDict['mobileNumber'] = "Mobile Number"
		dataDict['birthDate'] = "Birth Date"
		dataDict['username'] = "Username"
		dataDict['emailAddr'] = "Email Address"
		dataDict['password'] = "Password"
		dataDict['pswRepeat'] = "Repeat Password"
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr

	def checkMissingLoginFormKey(self, formRequest):
		dataStr = ""
		dataDict = dict()
		dataDict['usernameOrEmail'] = "Username or Email "
		dataDict['password'] = "Password "
		for x in dataDict:
			try:
				if((len(formRequest.POST[x]) > 0) == False):
					dataStr = dataDict[x] + " is missing."
					break
			except MultiValueDictKeyError:
				dataStr = dataDict[x] + " is missing."
				break
		return dataStr