from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from Employee.models import Employee, FamilyDetail, PreviousOrganization


class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        employee_list = Employee.objects.all()    
        context = {'employee_list' : employee_list}
        return render(request,'index.html', context)


# class EmployeeCreateView(View):
#     def get(self, request, *args, **kwargs):
#         employee_list = Employee.objects.all()    
#         context = {'employee_list' : employee_list}
#         return render(request,'employee_create.html', context)
    
#     def post(self, request, *args, **kwargs):
#         name = request.POST['name']    
#         salary = request.POST['salary']    
#         joining_date = request.POST['joining_date']    
#         employee = Employee.objects.create(name=name, salary=salary, joining_date=joining_date)
#         employee.save()
#         return JsonResponse({'status':'save'})

class EmployeeCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'employee_create.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']    
        salary = request.POST['salary']    
        joining_date = request.POST['joining_date']    
        employee = Employee.objects.create(name=name, salary=salary, joining_date=joining_date)
        employee.save()
        return JsonResponse({'status':'save','employee_id':employee.id})

class FamilyMemeberCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'employee_create.html')
    
    def post(self, request, *args, **kwargs):
        employee = Employee.objects.get(id=request.POST['employee_id'])
        member = request.POST['member']    
        relation_with_employee = request.POST['relation_with_employee']    
        profession = request.POST['profession']
        family_detail = FamilyDetail.objects.create(employees = employee, name=member, relation_with_employee = relation_with_employee, profession=profession)
        family_detail.save()
        return JsonResponse({'status':'save'})




class OrganizationCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'employee_create.html')
    def post(self, request, *args, **kwargs):
        employee = Employee.objects.get(id=request.POST['employee_id'])
        organization_name = request.POST['organization_name']    
        organization_description = request.POST['organization_description']    
        organization_detail = PreviousOrganization.objects.create(employees = employee, organization_name=organization_name, description=organization_description)
        organization_detail.save()
        return JsonResponse({'status':'save'})








class EmployeeEditView(View):

    def get(self, request, *args, pk, **kwargs):

 
        employee = Employee.objects.get(id=pk)
        employee_family_members = FamilyDetail.objects.select_related().filter(employees=employee)
        employee_previous_organization = PreviousOrganization.objects.select_related().filter(employees=employee)
        context = {
            'employee':employee,
            'employee_family_members':employee_family_members,
            'employee_previous_organization':employee_previous_organization
        }
        return render(request, 'employee_edit.html', context)

    def post(self, request, *args, pk, **kwargs):
        employee = Employee.objects.get(id=pk)
        if request.POST.get('name'):
            employee.name = request.POST.get('name')
        if request.POST.get('salary'):
            employee.salary = request.POST.get('salary')
        if request.POST.get('joining_date'):
            employee.joining_date = request.POST.get('joining_date')

        employee.save()
        return JsonResponse({'status': 'success', 'employee_id':employee.id})



class EmployeeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return redirect('employee_list')

class FamilyMemeberEditView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'employee_edit.html')

    def post(self, request, *args, **kwargs):
        family_member_id = request.POST.get('family_member_id')
        family_member_obj = FamilyDetail.objects.select_related().get(id=family_member_id)
        if request.POST.get('name'):
            family_member_obj.name = request.POST['name']
        if request.POST.get('relation_with_employee'):
            family_member_obj.relation_with_employee = request.POST['relation_with_employee'] 
        if request.POST.get('profession'):
            family_member_obj.profession = request.POST.get('profession') 
        family_member_obj.save()
        return HttpResponse('updated !!!!!!!!!!')


class OrganizationEditView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'employee_edit.html')

    def post(self, request, *args, **kwargs):
        organization_id = request.POST.get('organization_id')
        organization_Obj = PreviousOrganization.objects.select_related().get(id=organization_id)
        if request.POST.get('organization_name'):
            organization_Obj.organization_name = request.POST['organization_name']
        if request.POST.get('organization_description'):
            organization_Obj.description = request.POST['organization_description'] 
        organization_Obj.save()
        return HttpResponse('Updated !!!!!')

