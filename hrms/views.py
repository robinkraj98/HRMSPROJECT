from email.utils import formatdate
from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models  import Employee, Department, Employees,Kin, Attendance, Leave, Recruitment, Muster_wages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import RegistrationForm,LoginForm,EmployeeForm,KinForm,DepartmentForm,AttendanceForm, LeaveForm, RecruitmentForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
import datetime
from django.db.models import Count
from django.db import connection


def showdate(request):
    currentdate = datetime.date.today() 
    formatDate = currentdate.strftime("%b-%Y")
    return render(request, 'home.html', {Employees : data1, 'format_date':formatDate} )
    




# Create your views here.

from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django_xhtml2pdf.views import PdfMixin
from django_xhtml2pdf.utils import generate_pdf, render_to_pdf_response, pdf_decorator
from django.contrib.auth.models import User

# importing the necessary libraries
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from hrms import models,forms
#from .process import html_to_pdf 
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        print(form.is_valid())
        
        if form.is_valid()==False:
            user = authenticate(
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            
            if user is not None and user.is_superadmin:
                login(request, user)
                #message = f'Hello {user.username}!'
                return redirect('hrms:superadmin')
           
            elif user is not None and user.is_adminuser:
                login(request, user)
                #message = f'Hello {user.username}!'
                return redirect('hrms:adminuser')
            elif user is not None and user.is_employeeuser:
                login(request, user)
                #message = f'Hello {user.username}!'
                return redirect('hrms:employeeuser')
            elif user is not None and user.is_causer:
                login(request, user)
                #message = f'Hello {user.username}!'
                return redirect('hrms:causer')
            else:
                #message = 'Login failed!'
                message = ""
      
        
    
    return render(
        request, 'hrms/registrations/login.html', context={'form': form, 'message': message})

# Create your views here.
class Index(TemplateView):
   template_name = 'hrms/home/home.html'

#   Authentication
class Register (CreateView):
    model = get_user_model()
    form_class  = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')




    
class Login_View(LoginView):
    model = get_user_model()
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        url = resolve_url('hrms:dashboard')
        return url

class Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:login',permanent=True)
    
    
 # Main Board   
class Dashboard(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/index.html'
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employee.objects.order_by('-id')
        return context
class Superadmin_User(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/superadminindex.html'
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employee.objects.order_by('-id')
        return context
class Admin_User(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/adminindex.html'
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employee.objects.order_by('-id')
        return context
class Employee_User(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/employeeindex.html'
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employee.objects.order_by('-id')
        return context
class Ca_User(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/caindex.html'
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employee.objects.order_by('-id')
        return context
# Employee's Controller
class Employee_New(LoginRequiredMixin,CreateView):
    model = Employee  
    form_class = EmployeeForm  
    template_name = 'hrms/employee/create.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    
    
class Employee_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/employee/index.html'
    model = Employee
    login_url = 'hrms:login'
    context_object_name = 'employees'
    paginate_by  = 5
    
class Employeeuserforms_all(LoginRequiredMixin,ListView):
    template_name = 'hrms/employee/employeeuser_index.html'
    model = Employee
    login_url = 'hrms:login'
    context_object_name = 'employees'
    paginate_by  = 5 
class EmployeeUser_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/employee/employeeindex.html'
    model = Employee
    login_url = 'hrms:login'
    context_object_name = 'employees'
    paginate_by  = 5     
    
class Employee_View(LoginRequiredMixin,DetailView):
    queryset = Employee.objects.select_related('department')
    template_name = 'hrms/employee/single.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context
        
class Employee_Update(LoginRequiredMixin,UpdateView):
    model = Employee
    template_name = 'hrms/employee/edit.html'
    form_class = EmployeeForm
    login_url = 'hrms:login'
'''class Employee_Formsdownload(LoginRequiredMixin,UpdateView):
    model = Employee
    template_name = 'hrms/employee/allforms.html'
    form_class = EmployeeForm
    login_url = 'hrms:login'''
class Employee_Formsdownload(LoginRequiredMixin,DetailView):
    queryset = Employee.objects.select_related('department')
    template_name = 'hrms/employee/allforms.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context
    

        
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (LoginRequiredMixin,CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    login_url = 'hrms:login'
   

    def get_context_data(self):
        context = super().get_context_data()
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
            return context
        else:
            return context
class Employee_Formsdownload_user(LoginRequiredMixin,DetailView):
    queryset = Employee.objects.select_related('department')
    template_name = 'hrms/employee/employee_allforms.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context
    

        
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (LoginRequiredMixin,CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    login_url = 'hrms:login'
   

    def get_context_data(self):
        context = super().get_context_data()
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
            return context
        else:
            return context

class Employee_Kin_Update(LoginRequiredMixin,UpdateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_update.html'
    login_url = 'hrms:login'

    def get_initial(self):
        initial = super(Employee_Kin_Update,self).get_initial()
        
        if 'id' in self.kwargs:
            emp =  Employee.objects.get(pk=self.kwargs['id'])
            initial['employee'] = emp.pk
            
            return initial

#Department views

class Department_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'hrms/department/create.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')

#Attendance View

class Attendance_New (LoginRequiredMixin,CreateView):
    model = Attendance
    form_class = AttendanceForm
    login_url = 'hrms:login'
    template_name = 'hrms/attendance/create.html'
    success_url = reverse_lazy('hrms:attendance_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()
        pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate())) 
        context['present_staffers'] = pstaff
        return context

class Attendance_Out(LoginRequiredMixin,View):
    login_url = 'hrms:login'

    def get(self, request,*args, **kwargs):

       user=Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(status='PRESENT')& Q(date=timezone.localdate()))
       user.last_out=timezone.localtime()
       user.save()
       return redirect('hrms:attendance_new')   

class LeaveNew (LoginRequiredMixin,CreateView, ListView):
    model = Leave
    template_name = 'hrms/leave/create.html'
    form_class = LeaveForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:leave_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leaves"] = Leave.objects.all()
        return context

class Payroll(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    login_url = 'hrms:login'
    context_object_name = 'stfpay'

class RecruitmentNew (CreateView):
    model = Recruitment
    template_name = 'hrms/recruitment/index.html'
    form_class = RecruitmentForm
    success_url = reverse_lazy('hrms:recruitment')

class RecruitmentAll(LoginRequiredMixin,ListView):
    model = Recruitment
    login_url = 'hrms:login'
    template_name = 'hrms/recruitment/all.html'
    context_object_name = 'recruit'

class RecruitmentDelete (LoginRequiredMixin,View):
    login_url = 'hrms:login'
    def get (self, request,pk):
     form_app = Recruitment.objects.get(pk=pk)
     form_app.delete()
     return redirect('hrms:recruitmentall', permanent=True)

class Pay(LoginRequiredMixin,ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    context_object_name = 'emps'
    login_url = 'hrms:login'



def test_view(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('test_pdf.html', file_object=resp)
    return result



def test_view_fileobject(request):
    # this test file_object as None in py2 and py3
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('test_pdf.html')
    result.seek(0)
    resp.write(result.read())
    return resp


def test_render_response(request):
    return render_to_pdf_response('test_pdf.html')

@pdf_decorator
def render_template_decorated(request):
    return render(request, 'test_pdf.html')

class UserPdfView(PdfMixin, DetailView):
    model = User
    template_name = "user_pdf.html"
    
  

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
#Creating a class based view
class GeneratePdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        open('templates/temp.html', "w").write(render_to_string('result.html', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
class EmployementCardPdf(View):
    def get(self, request, pk=None,*args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        data1 = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('employmentcardstemp.html', {'Employees': data,'Muster':data1}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#Service Certificate
class ServiceCertificatePdf(View):
    def get(self, request, pk=None,*args, **kwargs):
        #data = models.Employees.objects.all()
        data = models.Employees.objects.get(pk=pk)    
    #def get(self, request, *args, **kwargs):
     #   data = models.Employee.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('servicecertificatetemp.htm', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#leave Register
class LeaveRegisterPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        #data = models.Employees.objects.all().order_by('first_name')
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('leaveregistertemp.htm', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#wage slip
class WageSlipPdf(View):
    def get(self, request, pk=None,*args, **kwargs):
        #data = models.Employees.objects.all()
        data = models.Employees.objects.get(pk=pk)
        #data=get_object_or_404(models.Employees,pk="1")
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('wagesliptemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


#Deductions
class DeductionsPdf(View):
     def get(self, request, pk=None,*args, **kwargs):
        #data = models.Employees.objects.all()
        data = models.Employees.objects.get(pk=pk)
    
    #def get(self, request, *args, **kwargs):
        #data = models.Employee.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('deductionstemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


class FinesPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('finestemp.html',{'Employees':data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class AdvancesPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('advancestemp.html', {'Employees':data,'formatDate':formatDate }))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


class OvertimePdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        open('templates/temp.html', "w").write(render_to_string('overtimetemp.html', {'data': data}))
        #below_15 = models.Employees.objects.filter(Gross_Wages_Payable_or_Total_Amount__lt=20000).count()
        below_15 = models.Employees.objects.filter(Q(Gross_Wages_Payable_or_Total_Amount__gt=0) & Q(Gross_Wages_Payable_or_Total_Amount__lt=15000 )).count()
        above_15 = models.Employees.objects.filter(Q(Gross_Wages_Payable_or_Total_Amount__gt=15000) & Q(Gross_Wages_Payable_or_Total_Amount__lt=20000 )).count()
        above_20 = models.Employees.objects.filter(Gross_Wages_Payable_or_Total_Amount__gte=20000).count()
        
        #pubs = Publisher.objects.annotate(below_15=below_15).annotate(above_15=above_15)
        print(above_15*150)
        print(below_15*0)
        print(above_20*200)

        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
    
    
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('overtimetemp.html', {'Employees': data,'formatDate':formatDate }))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class FormAPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formAtemp.html', {'Employees':data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class EsiInspectionPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('esi_inspectiontemp.html', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class EpfInspectionPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('epf_inspectiontemp.htm', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class FormVPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.all().get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        below_15 = models.Employees.objects.filter(Q(Gross_Wages_Payable_or_Total_Amount__gt=0) & Q(Gross_Wages_Payable_or_Total_Amount__lt=15000 )).count()
        above_15 = models.Employees.objects.filter(Q(Gross_Wages_Payable_or_Total_Amount__gt=15000) & Q(Gross_Wages_Payable_or_Total_Amount__lt=20000 )).count()
        above_20 = models.Employees.objects.filter(Gross_Wages_Payable_or_Total_Amount__gte=20000).count()

        below_15_total = models.Employees.objects.filter(Q(Gross_Wages_Payable_or_Total_Amount__gt=0) & Q(Gross_Wages_Payable_or_Total_Amount__lt=15000 )).count()*0
        above_15_total= models.Employees.objects.filter(Q(Gross_Wages_Payable_or_Total_Amount__gt=15000) & Q(Gross_Wages_Payable_or_Total_Amount__lt=20000 )).count()*150
        above_20_total= models.Employees.objects.filter(Gross_Wages_Payable_or_Total_Amount__gte=20000).count()*200
        
        #pubs = Publisher.objects.annotate(below_15=below_15).annotate(above_15=above_15)
        print(above_15*150)
        print(below_15*0)
        print(above_20*200)
        total=(above_15*150)+(below_15*0)+(above_20*200)
        print(total)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formVtemp.html', {'Employees': data,'formatDate':formatDate,'above_15':above_15,'below_15':below_15,'above_20':above_20,'total':total}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


class EqualRemunerationPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('equalremunerationtemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


class MusterRollPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('muster_rolltemp.html', {'Employees': data, 'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class WagesRegPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('wagesregtemp.html', {'Employees': data, 'formatDate':formatDate}))
        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class BankUploadPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('bankuploadtemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class AccidentPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('accidenttemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class BonusPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('bonustemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




class FormBPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formBtemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class FormCPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formCtemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class FormDPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formDtemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class FormEPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formEtemp.html', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class MISPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #att_days = models.Employees.objects.all().aggregate(sum('Payable_days'))
        att_days=0
        insurance_contribution='NIL'
        maternity_benefit_contribution='NIL'
        bonus_contribution=72100
        Gratuity_Contribution='NIL'
        
        cursor = connection.cursor()
        print(cursor.execute('SELECT sum(Payable_days),sum(Gross_Wages_Payable_or_Total_Amount),sum(esi),sum(PF_Amount),sum(PT_Amount),sum(TDS_Amount),sum(Net_Salary) FROM hrms.hrms_employees'))
        row = cursor.fetchone()
        
        att_days=str(row[0])
        Emp_total_amt=str(row[1])
        esi_total=str(row[2])
        esi_employer_total=round((row[2]*3.25)/0.75,2)
        epf_total=str(row[3])
        epf_employer_total=round((row[3]*13)/12,2)
        pt_contribution=str(row[4])
        tds_contribution=str(row[5])
        net_salary=str(row[6])

        
       
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('mistemp.html', {'Gratuity_Contribution':Gratuity_Contribution,'bonus_contribution':bonus_contribution,'net_salary':net_salary,'tds_contribution':tds_contribution,'pt_contribution':pt_contribution,'maternity_benefit_contribution':maternity_benefit_contribution,'insurance_contribution':insurance_contribution,'epf_employer_total':epf_employer_total,'esi_employer_total':esi_employer_total,'epf_total':epf_total,'esi_total':esi_total,'Emp_total_amt':Emp_total_amt,'att_days':att_days,'Employees': data,'formatDate':formatDate }))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class IntegrateAnnualReturnPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('integrateannualreturntemp.html', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class PoshPdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Employee.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('poshtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class WorkmenRegPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('workmenregtemp.html', {'Employees': data,'formatDate':formatDate }))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


class MasterPdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Employees.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('mastertemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class ESImcPdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Employee.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('esimctemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class EpfEcrPdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Employee.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('epfecrtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class TdsPdf(View):
    def get(self, request, *args, **kwargs):
        data = models.Employee.objects.all().order_by('first_name')
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('tdstemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



class LabourInseptionPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('labourinceptiontemp.html', {'Employees': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')





class DeductionsPdf(View):
    def get(self, request,pk=None, *args, **kwargs):
        data = models.Employees.objects.get(pk=pk)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
    
    
        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('deductionstemp.html', {'Employees': data,'formatDate':formatDate }))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')





#Muster_wages

def fineslistpage(request):
    obj=Employee.objects.all()
    return render(request,'finestest.html',{'obj':obj})
def finesdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'finestemp.html',{'obj':obj})
def getfines(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('finestemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


#Muster_wages

def advanceslistpage(request):
    obj=Employee.objects.all()
    return render(request,'advancestest.html',{'obj':obj})
def advancesdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'advancestemp.html',{'obj':obj})
def getadvances(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('advancestemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




#Muster_wages

def overtimelistpage(request):
    obj=Employee.objects.all()
    return render(request,'overtimetest.html',{'obj':obj})
def overtimedetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'overtimetemp.html',{'obj':obj})
def getovertime(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        datad=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))
        

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
       

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




#Muster_wages

def formalistpage(request):
    obj=Employee.objects.all()
    return render(request,'formatest.html',{'obj':obj})
def formadetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'formAtemp.html',{'obj':obj})
def getforma(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formAtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


#Muster_wages

def esiinspectionlistpage(request):
    obj=Employee.objects.all()
    return render(request,'esiinspectiontest.html',{'obj':obj})
def esiinspectiondetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'esi_inspectiontemp.html',{'obj':obj})
def getesiinspection(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('esi_inspectiontemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




#Muster_wages

def epfinspectionlistpage(request):
    obj=Employee.objects.all()
    return render(request,'epfinspectiontest.html',{'obj':obj})
def epfinspectiondetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'epf_inspectiontemp.html',{'obj':obj})
def getepfinspection(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('epf_inspectiontemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def formvlistpage(request):
    obj=Employees.objects.all()
    return render(request,'formvtest.html',{'Employees': data,'formatDate':formatDate})
def formvdetail(request,id):
    obj=get_object_or_404(Employees,pk=id)
    return render(request,'formVtemp.html',{'Employees': data,'formatDate':formatDate})
def getformv(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employees,pk=id)
        currentdate = datetime.date.today()
        print(currentdate) 
        formatDate = currentdate.strftime("%b-%y")
        print(formatDate)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('formVtemp.html', {'Employees': data,'formatDate':formatDate}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




#Muster_wages

def equalremlistpage(request):
    obj=Employee.objects.all()
    return render(request,'equalremtest.html',{'obj':obj})
def equalremdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'equalremunerationtemp.html',{'obj':obj})
def getequalrem(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('equalremunerationtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def bankuploadlistpage(request):
    obj=Employee.objects.all()
    return render(request,'bankuploadtest.html',{'obj':obj})
def bankuploaddetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'bankuploadtemp.html',{'obj':obj})
def getbankupload(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('bankuploadtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def accidentlistpage(request):
    obj=Employee.objects.all()
    return render(request,'accidenttest.html',{'obj':obj})
def accidentdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'accidenttemp.html',{'obj':obj})
def getaccident(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('accidenttemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




#Muster_wages

def mislistpage(request):
    obj=Employee.objects.all()
    return render(request,'mistest.html',{'obj':obj})
def misdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'mistemp.html',{'obj':obj})
def getmis(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('mistemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


#Muster_wages

def poshlistpage(request):
    obj=Employee.objects.all()
    return render(request,'poshtest.html',{'obj':obj})
def poshdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'poshtemp.html',{'obj':obj})
def getposh(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('poshtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




def tdslistpage(request):
    obj=Employee.objects.all()
    return render(request,'tdstest.html',{'obj':obj})
def tdsdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'tdstemp.html',{'obj':obj})
def gettds(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('tdstemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


#Muster_wages

def muster_rolllistpage(request):
    obj=Employee.objects.all()
    return render(request,'muster_rolltest.html',{'obj':obj})
def muster_rolldetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'muster_rolltemp.html',{'obj':obj})
def getmuster_roll(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('muster_rolltemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




#Muster_wages

def wagesreglistpage(request):
    obj=Employee.objects.all()
    return render(request,'wagesregtest.html',{'obj':obj})
def wagesregdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'wagesregtemp.html',{'obj':obj})
def getwagesreg(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('wagesregtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def integrateannualreturnlistpage(request):
    obj=Employee.objects.all()
    return render(request,'integrateannualreturntest.html',{'obj':obj})
def integrateannualreturndetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'integrateannualreturntemp.html',{'obj':obj})
def getintegrateannualreturn(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('integrateannualreturntemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



def workmenreglistpage(request):
    obj=Employee.objects.all()
    return render(request,'workmenregtest.html',{'obj':obj})
def workmenregdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'workmenregtemp.html',{'obj':obj})
def getworkmenreg(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('workmenregtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def esimclistpage(request):
    obj=Employee.objects.all()
    return render(request,'esimctest.html',{'obj':obj})
def esimcdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'esimctemp.html',{'obj':obj})
def getesimc(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('esimctemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def epfecrlistpage(request):
    obj=Employee.objects.all()
    return render(request,'epfecrtest.html',{'obj':obj})
def epfecrdetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'epfecrtemp.html',{'obj':obj})
def getepfecr(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('epfecrtemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



#Muster_wages

def labourinceptionlistpage(request):
    obj=Employee.objects.all()
    return render(request,'labourinceptiontest.html',{'obj':obj})
def labourinceptiondetail(request,id):
    obj=get_object_or_404(Employee,pk=id)
    return render(request,'labourinceptiontemp.html',{'obj':obj})
def getlabourinception(request,id):
        #data = models.Employee.objects.all().order_by('first_name')
        data=get_object_or_404(Employee,pk=id)
        #open('templates/employmentcardstemp.html', "w" ).write(render_to_string('employmentcards.html', {'data': data}))

        # Converting the HTML template into a PDF file
        #pdf = html_to_pdf('employmentcardstemp.html')
        open('templates/temp.html', "w").write(render_to_string('labourinceptiontemp.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')









