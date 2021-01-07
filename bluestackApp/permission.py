from .models import User
from rest_framework import permissions
from .CommonEnum import UserType
class AdminPermission(permissions.BasePermission):
# Token: edccdbe42699795f832d543f61f6815bc535f544
    def has_permission(self, request, view):
    	if request.user.has_perm('auth.view_user'):
    		return True
    	else:
	    	return False
class IsEnggManager(permissions.BasePermission):
    def has_permission(self,request,view):
        emobj= User.objects.get(id=request.user.id)
        if emobj.user_type == UserType.ENGG_MANAGER:
          return True
        else:
          return False

class IsOfficeManager(permissions.BasePermission):

    def has_permission(self,request,view):
        emobj= User.objects.get(id=request.user.id)
        if emobj.user_type == UserType.OFFICE_MANAGER:
          return True
        else:
          return False
class IsEmployee(permissions.BasePermission):
    def has_permission(self,request,view):
        emobj= User.objects.get(id=request.user.id)
        if emobj.user_type == UserType.EMPLOYEE:
            return True
        else:
          return False