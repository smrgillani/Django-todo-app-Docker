from ..DAL.CategoriesDAL import CategoriesDAL as ct
from ..Models.Category import Category

class CategoriesBL():

	def allCategories(icv):
		act = ct.allCategories(icv)
		Categories = list()
		for i in act:
			cty = Category()
			cty.Id = i.c_id
			cty.title = i.title
			cty.isActive = i.isActive
			Categories.append(cty)
		return Categories

	def addCategory(ico):
		rcto = ct.addCategory(ico)
		cty = Category();
		cty.Id = rcto.c_id
		return cty

	def selectCategory(ico):
		rcto = ct.selectOneCategory(ico)
		cty = Category();
		cty.Id = rcto.c_id
		cty.title = rcto.title
		cty.isActive = rcto.isActive
		return cty

	def updateCategory(ico):
		rcto = ct.updateCategory(ico)
		cty = Category();
		cty.Id = rcto.c_id
		return cty

	def deleteCategory(ico):
		rcto = ct.deleteCategory(ico)
		return rcto