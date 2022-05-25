



from django.contrib import admin
from django.urls import include,path
from Employee.views import EmployeeListView, EmployeeEditView, EmployeeDeleteView, EmployeeCreateView, FamilyMemeberCreateView, OrganizationCreateView


urlpatterns = [
    path('', EmployeeListView.as_view(), name="employee_list"), 
    path('edit/<str:pk>', EmployeeEditView.as_view(), name="employee_edit"), 
    path('delete/<str:pk>', EmployeeDeleteView.as_view(), name="employee_delete"), 
    path('create/', EmployeeCreateView.as_view(), name="employee_create"), 
    
    
    path('FamilyMemeberCreate/', FamilyMemeberCreateView.as_view(), name="family_member_create"), 
    path('OranizationMemeberCreate/', OrganizationCreateView.as_view(), name="organization_create"), 


]
