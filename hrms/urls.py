from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from hrms.views import showdate, test_view, test_render_response, UserPdfView,render_template_decorated, test_view_fileobject
from hrms.views import GeneratePdf,EmployementCardPdf, ServiceCertificatePdf, LeaveRegisterPdf, WageSlipPdf, DeductionsPdf, FinesPdf, AdvancesPdf, OvertimePdf, FormAPdf, EsiInspectionPdf, EpfInspectionPdf, FormVPdf, EqualRemunerationPdf,EmployeeUser_All,Employee_Formsdownload_user
from hrms.views import MusterRollPdf, WagesRegPdf,BankUploadPdf, AccidentPdf, BonusPdf, FormBPdf, FormCPdf, FormDPdf, FormEPdf, MISPdf, IntegrateAnnualReturnPdf
from hrms.views import PoshPdf, WorkmenRegPdf, MasterPdf, ESImcPdf,EpfEcrPdf, TdsPdf, LabourInseptionPdf




from hrms.views import finesdetail, fineslistpage, getfines
from hrms.views import advancesdetail, advanceslistpage, getadvances
from hrms.views import overtimedetail, overtimelistpage, getovertime
from hrms.views import formadetail, formalistpage, getforma
from hrms.views import esiinspectiondetail, esiinspectionlistpage, getesiinspection
from hrms.views import epfinspectiondetail, epfinspectionlistpage, getepfinspection
from hrms.views import formvdetail, formvlistpage, getformv
from hrms.views import equalremdetail, equalremlistpage, getequalrem
from hrms.views import bankuploaddetail, bankuploadlistpage, getbankupload
from hrms.views import accidentdetail, accidentlistpage, getaccident
from hrms.views import misdetail, mislistpage, getmis
from hrms.views import poshdetail, poshlistpage, getposh
from hrms.views import tdsdetail, tdslistpage, gettds
from hrms.views import muster_rolldetail, muster_rolllistpage, getmuster_roll
from hrms.views import wagesregdetail, wagesreglistpage, getwagesreg
from hrms.views import integrateannualreturndetail, integrateannualreturnlistpage, getintegrateannualreturn
from hrms.views import workmenregdetail, workmenreglistpage, getworkmenreg
from hrms.views import esimcdetail, esimclistpage, getesimc
from hrms.views import epfecrdetail, epfecrlistpage, getepfecr
from hrms.views import labourinceptiondetail, labourinceptionlistpage, getlabourinception,Employeeuserforms_all,Employee_Formsdownload_user




app_name = 'hrms'
urlpatterns = [

# Authentication Routes
    path('', views.Index.as_view(), name='index'),
   
    path('register/', views.Register.as_view(), name='reg'),
    path('loginpage/', views.login_page, name='loginpage'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('superadmin/', views.Superadmin_User.as_view(), name='superadmin'),
    path('adminuser/', views.Admin_User.as_view(), name='adminuser'),
    path('employeeuser/', views.Employee_User.as_view(), name='employeeuser'),
    path('employeeuser_all/', views.EmployeeUser_All.as_view(), name='employeeuser_all'),
     path('causer/', views.Ca_User.as_view(), name='causer'),

# Employee Routes
    path('dashboard/employee/', views.Employee_All.as_view(), name='employee_all'),
    path('dashboard/employee/<int:pk>/downloadforms/', views.Employee_Formsdownload.as_view(), name='Employee_Formsdownload'),
    path('dashboard/employeeuser/', views.EmployeeUser_All.as_view(), name='employeeuser'),
    
     path('dashboard/employeeuser/<int:pk>/downloadforms/', views.Employee_Formsdownload_user.as_view(), name='Employee_Formsdownload_user'),
    
    
    
    path('dashboard/employee/<int:pk>/downloadforms/getformb', views.FormBPdf.as_view(), name='getformb'),
    path('dashboard/employee/new/', views.Employee_New.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
    path('dashboard/employee/<int:pk>/update/', views.Employee_Update.as_view(), name='employee_update'),
    path('dashboard/employee/<int:pk>/delete/', views.Employee_Delete.as_view(), name='employee_delete'),
    path('dashboard/employee/<int:id>/kin/add/', views.Employee_Kin_Add.as_view(), name='kin_add'),
    path('dashboard/employee/<int:id>/kin/<int:pk>/update/', views.Employee_Kin_Update.as_view(), name='kin_update'),

#Department Routes
    path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
    path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),

#Attendance Routes
    path('dashboard/attendance/in/', views.Attendance_New.as_view(), name='attendance_new'),
    path('dashboard/attendance/<int:pk>/out/', views.Attendance_Out.as_view(), name='attendance_out'),

#Leave Routes

    path("dashboard/leave/new/", views.LeaveNew.as_view(), name="leave_new"),

#Recruitment

    path("recruitment/",views.RecruitmentNew.as_view(), name="recruitment"),
    path("recruitment/all/",views.RecruitmentAll.as_view(), name="recruitmentall"),
    path("recruitment/<int:pk>/delete/", views.RecruitmentDelete.as_view(), name="recruitmentdelete"),

#Payroll
    path("employee/pay/",views.Pay.as_view(), name="payroll"),
    path('dashboard/employee/<int:pk>/downloadforms/pdf/', GeneratePdf.as_view(),name="payslip"),
    #path('empcardpdf/', EmployementCardPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/empcardpdf', views.EmployementCardPdf.as_view(), name='getempcard'),
    #path('servicepdf/', ServiceCertificatePdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/servicepdf', views.ServiceCertificatePdf.as_view(), name='servicepdf'),
    #path('leavepdf/', LeaveRegisterPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/leavepdf', views.LeaveRegisterPdf.as_view(), name='leavepdf'),
    #path('wagepdf/', WageSlipPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/wagepdf', views.WageSlipPdf.as_view(), name='wagepdf'),
    #path('deductionspdf/', DeductionsPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/deductionspdf', views.DeductionsPdf.as_view(), name='deductionspdf'),
    #path('finespdf/', FinesPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/finespdf', views.FinesPdf.as_view(), name='finespdf'),
    #path('advancespdf/', AdvancesPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/advancespdf', views.AdvancesPdf.as_view(), name='advancespdf'),
    #path('overtimepdf/', OvertimePdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/overtimepdf', views.OvertimePdf.as_view(), name='overtimepdf'),
    #path('formApdf/', FormAPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/formApdf', views.FormAPdf.as_view(), name='formApdf'),
    path('esiinspectionpdf/', EsiInspectionPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/esiinspectionpdf', views.EsiInspectionPdf.as_view(), name='esiinspectionpdf'),
    #path('epfinspectionpdf/', EpfInspectionPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/epfinspectionpdf', views.EpfInspectionPdf.as_view(), name='epfinspectionpdf'),
    #path('formvpdf/', FormVPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/formvpdf', views.FormVPdf.as_view(), name='formvpdf'),
    #path('equalremunerationpdf/', EqualRemunerationPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/equalremunerationpdf', views.EqualRemunerationPdf.as_view(), name='equalremunerationpdf'),
    #path('musterrollpdf/', MusterRollPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/musterrollpdf', views.MusterRollPdf.as_view(), name='musterrollpdf'),
    #path('wagesregpdf/', WagesRegPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/wagesregpdf', views.WagesRegPdf.as_view(), name='wagesregpdf'),
    #path('bankuploadpdf/', BankUploadPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/bankuploadpdf', views.BankUploadPdf.as_view(), name='bankuploadpdf'),
    #path('accidentpdf/', AccidentPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/accidentpdf', views.AccidentPdf.as_view(), name='accidentpdf'),
    #path('bonuspdf/', BonusPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/bonuspdf', views.BonusPdf.as_view(), name='bonuspdf'),
    #path('formbpdf/', FormBPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/formbpdf', views.FormBPdf.as_view(), name='formbpdf'),
    #path('formcpdf/', FormCPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/formcpdf', views.FormCPdf.as_view(), name='formcpdf'),
    #path('formdpdf/', FormDPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/formdpdf', views.FormDPdf.as_view(), name='formdpdf'),
    #path('formepdf/', FormEPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/formepdf', views.FormEPdf.as_view(), name='formepdf'),
    #path('mispdf/', MISPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/mispdf', views.MISPdf.as_view(), name='mispdf'),
    #path('annualreturnpdf/', IntegrateAnnualReturnPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/annualreturnpdf', views.IntegrateAnnualReturnPdf.as_view(), name='annualreturnpdf'),
    path('poshpdf/', PoshPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/poshpdf', views.PoshPdf.as_view(), name='poshpdf'),
    path('workmenpdf/', WorkmenRegPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/workmenpdf', views.WorkmenRegPdf.as_view(), name='workmenpdf'),
    path('masterpdf/', MasterPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/masterpdf', views.MasterPdf.as_view(), name='masterpdf'),
    #path('esimcpdf/', ESImcPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/esimcpdf', views.ESImcPdf.as_view(), name='esimcpdf'),
    #path('epfecrpdf/', EpfEcrPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/epfecrpdf', views.EpfEcrPdf.as_view(), name='epfecrpdf'),
    #path('tdspdf/', TdsPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/tdspdf', views.TdsPdf.as_view(), name='tdspdf'),
    #path('labourinspectionpdf/', LabourInseptionPdf.as_view()),
    path('dashboard/employee/<int:pk>/downloadforms/labourinspectionpdf', views.LabourInseptionPdf.as_view(), name='labourinspectionpdf'),
  
     path('dashboard/employee/<int:pk>/downloadforms/deductionsPdf', views.DeductionsPdf.as_view(), name='deductionsPdf'),
    #path('detail',detail,name='detail'),




     
    

    path('<int:id>',finesdetail,name='finesdetail'),
    path('<int:id>',getfines,name='getfines'),
    url(r'^finestest/', fineslistpage),



    path('<int:id>',advancesdetail,name='advancesdetail'),
    path('<int:id>',getadvances,name='getadvances'),
    url(r'^advancestest/', advanceslistpage),
    

    path('<int:id>',overtimedetail,name='overtimedetail'),
    path('<int:id>',getovertime,name='getovertime'),
    url(r'^overtimetest/', overtimelistpage),



    path('<int:id>',formadetail,name='formadetail'),
    path('<int:id>',getforma,name='getforma'),
    url(r'^formatest/', formalistpage),



    path('<int:id>',esiinspectiondetail,name='esiinspectiondetail'),
    path('<int:id>',getesiinspection,name='getesiinspection'),
    url(r'^esiinspectiontest/', esiinspectionlistpage),



    path('<int:id>',epfinspectiondetail,name='epfinspectiondetail'),
    path('<int:id>',getepfinspection,name='getepfinspection'),
    url(r'^epfinspectiontest/', epfinspectionlistpage),


    path('<int:id>',formvdetail,name='formvdetail'),
    path('<int:id>',getformv,name='getformv'),
    url(r'^formvtest/', formvlistpage),

    path('<int:id>',equalremdetail,name='equalremdetail'),
    path('<int:id>',getequalrem,name='getequalrem'),
    url(r'^equalremtest/', equalremlistpage),


    path('<int:id>',bankuploaddetail,name='bankuploaddetail'),
    path('<int:id>',getbankupload,name='getbankupload'),
    url(r'^bankuploadtest/', bankuploadlistpage),


    path('<int:id>',accidentdetail,name='accidentdetail'),
    path('<int:id>',getaccident,name='getaccident'),
    url(r'^accidenttest/', accidentlistpage),

    path('<int:id>',misdetail,name='misdetail'),
    path('<int:id>',getmis,name='getmis'),
    url(r'^mistest/', mislistpage),

    path('<int:id>',poshdetail,name='poshdetail'),
    path('<int:id>',getposh,name='getposh'),
    url(r'^poshtest/', poshlistpage),

    path('<int:id>',tdsdetail,name='tdsdetail'),
    path('<int:id>',gettds,name='gettds'),
    url(r'^tdstest/', tdslistpage),

    path('<int:id>',muster_rolldetail,name='muster_rolldetail'),
    path('<int:id>',getmuster_roll,name='getmuster_roll'),
    url(r'^muster_rolltest/', muster_rolllistpage),


    path('<int:id>',wagesregdetail,name='wagesregdetail'),
    path('<int:id>',getwagesreg,name='getwagesreg'),
    url(r'^wagesregtest/', wagesreglistpage),


    path('<int:id>',integrateannualreturndetail,name='integrateannualreturndetail'),
    path('<int:id>',getintegrateannualreturn,name='getintegrateannualreturn'),
    url(r'^integrateannualreturntest/', integrateannualreturnlistpage),

    path('<int:id>',workmenregdetail,name='workmenregdetail'),
    path('<int:id>',getworkmenreg,name='getworkmenreg'),
    url(r'^workmenregtest/', workmenreglistpage),

    path('<int:id>',esimcdetail,name='esimcdetail'),
    path('<int:id>',getesimc,name='getesimc'),
    url(r'^esimctest/', esimclistpage),


    path('<int:id>',epfecrdetail,name='epfecrdetail'),
    path('<int:id>',getepfecr,name='getepfecr'),
    url(r'^epfecrtest/', epfecrlistpage),

    path('<int:id>',labourinceptiondetail,name='labourinceptiondetail'),
    path('<int:id>',getlabourinception,name='getlabourinception'),
    url(r'^labourinceptiontest/', labourinceptionlistpage),





    url(r'^admin/', admin.site.urls),
    url(r'^test_view$', test_view),
    url(r'^test_render_response$', test_render_response),
    url(r'^test_view_fileobject$', test_view_fileobject),
    url(r'^test_user/(?P<pk>\d+)$', UserPdfView.as_view()),
    url(r'^render_template_decorated$',render_template_decorated)



]


