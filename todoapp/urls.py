"""foodapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
"""
from .FolderName.FileName import ClassName

upper statement means import a class from a file which exist in a folder 

.			=>	current Folder where urls.py reside
FolderName	=>	Controllers is a folder name
FileName	=>	MyClass is a file which exists in Controllers folder as MyClass.py
ClassName	=>	MyClass is Python class which syntax exists in MyClass.py

"""
from .Controllers import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:question_id>/', myclass.MyClass().detail, name='detail'),
    path('', UserController.UserController().userDashboard, name='userDashboard',),
    path('register', UserController.UserController().userSignup, name='userSignup'),
    path('loginrd', UserController.UserController().userLoginRd, name='userLoginRd'),
    path('login', UserController.UserController().userLogin, name='userLogin'),
    path('logout', UserController.UserController().userLogout, name='userLogout'),

    #Todo Categories
    path('categories', TodoCategoryController.TodoCategoryController().allCategories, name='allCategories',),
    path('category', TodoCategoryController.TodoCategoryController().addUpdateCategory, name='addUpdateCategory',),
    path('category/<int:cate_id>/', TodoCategoryController.TodoCategoryController().addUpdateCategory, name='addUpdateCategory',),
    path('delcategory/<int:cate_id>/', TodoCategoryController.TodoCategoryController().removeCategory, name='removeCategory',),
    #Todo Categories
    #path('tasks', TodoTaskController.TodoTaskController().allCategories, name='allCategories',),
    path('task', TodoTaskController.TodoTaskController().addUpdateTask, name='addUpdateTask',),
    path('task/<int:task_id>/', TodoTaskController.TodoTaskController().addUpdateTask, name='addUpdateTask',),
    path('deltask/<int:task_id>/', TodoTaskController.TodoTaskController().removeTask, name='removeTask',),
    path('sharetask', TodoTaskController.TodoTaskController().shareTask, name='shareTask',),
]
