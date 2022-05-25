from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from Employee.models import Employee, FamilyDetail, PreviousOrganization


class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        employee_list = Employee.objects.all()    
        context = {'employee_list' : employee_list}
        return render(request,'index.html', context)


class EmployeeCreateView(View):
    def get(self, request, *args, **kwargs):
        employee_list = Employee.objects.all()    
        context = {'employee_list' : employee_list}
        return render(request,'employee_create.html', context)
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']    
        salary = request.POST['salary']    
        joining_date = request.POST['joining_date']    
        employee = Employee.objects.create(name=name, salary=salary, joining_date=joining_date)
        employee.save()
        return JsonResponse({'status':'save'})

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

    def get(self, request, *args, **kwargs):

        return render(request, 'employee_edit.html')

    def post(self, request, *args, **kwargs):

        return HttpResponse('post edit')

class EmployeeDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return redirect('employee_list')

