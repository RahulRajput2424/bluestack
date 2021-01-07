from .models import User
from rest_framework import permissions

class AdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
    	if request.user.has_perm('auth.view_user'):
    		return True
    	else:
	    	return False
# class IsEnggManager(permissions.BasePermission):
#     def has_permission(self,request,view):
#     	if User.objects.filter(id=request.user.id).user_type
    	

    		
