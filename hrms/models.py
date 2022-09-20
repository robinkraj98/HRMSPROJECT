from pyexpat import model
from django.db import models
import random

from django.db import models
from django.db.models import Model
from django.urls import reverse
from django.utils import timezone
import time
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    thumb = models.ImageField()
    is_superadmin=models.BooleanField('Is Superadmin',default=False)
    is_adminuser=models.BooleanField('Is Adminuser',default=False)
    is_employeeuser=models.BooleanField('Is Employeeuser',default=False)
    is_causer=models.BooleanField('Is Causer',default=False)


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hrms:dept_detail", kwargs={"pk": self.pk})
    

class Employee(models.Model):
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    nuban = models.CharField(max_length=10, default='0123456789')
    bank = models.CharField(max_length=25, default='First Bank Plc')
    salary = models.CharField(max_length=16,default='00,000.00')      
    def __str__(self):
        return self.first_name
        
    def get_absolute_url(self):
        return reverse("hrms:employee_view", kwargs={"pk": self.pk})
    

class Kin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.first_name+'-'+self.last_name
    
    def get_absolute_url(self):
        return reverse("hrms:employee_view",kwargs={'pk':self.employee.pk})
    

class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField()
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def save(self,*args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance,self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)

class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start

class Recruitment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    position = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name +' - '+self.position

        
class Employees(models.Model):
    Serial_No=models.CharField(max_length=30)
    Service_Status=models.CharField(max_length=30)
    Work_Location=models.CharField(max_length=30)
    Name_of_the_Principal_Employer=models.CharField(max_length=30)
    h_no_street_name=models.CharField(max_length=30)
    Village_Name=models.CharField(max_length=30)
    Mandal_District_Name=models.CharField(max_length=30)
    State_with_PIN_code=models.CharField(max_length=30)
    Employee_ID=models.CharField(max_length=30)
    Serial_no_Register_of_Workmen=models.CharField(max_length=30)
    Name_Employeer_Aadhar_Card=models.CharField(max_length=30)
    Date_of_Birth=models.CharField(max_length=30)
    sex=models.CharField(max_length=30)
    Marital_Status=models.CharField(max_length=30)
    Father_Name=models.CharField(max_length=30)
    Husband_Wife_Name=models.CharField(max_length=30)
    Department=models.CharField(max_length=30)
    Designation_Nature_of_Work_Done=models.CharField(max_length=30)
    permanent_h_no_street_name=models.CharField(max_length=30)
    permanent_Village_Name=models.CharField(max_length=30)
    permanent_Mandal_District_Name=models.CharField(max_length=30)
    permanent_State_with_PIN_code=models.CharField(max_length=30)
    present_h_no_street_name=models.CharField(max_length=30)
    present_Village_Name=models.CharField(max_length=30)
    present_Mandal_District_Name=models.CharField(max_length=30)
    present_State_with_PIN_code=models.CharField(max_length=30)
    Date_of_Joining=models.CharField(max_length=30)
    Specimen_Signature_or_thumb_of_Workman=models.CharField(max_length=30)
    Date_of_termination_of_Employment=models.CharField(max_length=30)
    Reasons_for_termination=models.CharField(max_length=30)
    Performance_Remarks=models.CharField(max_length=30)
    EPF_UAN_Number_IfExists_Already=models.CharField(max_length=30)
    ESI_Number_If_Already_Exists=models.CharField(max_length=30)
    Bank_Name=models.CharField(max_length=30)
    Bank_Account_No=models.CharField(max_length=30)
    Bank_IFSC_Code=models.CharField(max_length=30)
    Aadhar_Card_No=models.CharField(max_length=30)
    PAN_No=models.CharField(max_length=30)
    Mobile=models.CharField(max_length=30)
    Emergency_Contact_Number=models.CharField(max_length=30)
    Mail_ID=models.CharField(max_length=30)
    Nationality=models.CharField(max_length=30)
    Educational_Qualification=models.CharField(max_length=30)
    Identification_Marks=models.CharField(max_length=30)
    Blood_Group=models.CharField(max_length=30)
    Height=models.CharField(max_length=30)
    Weight=models.CharField(max_length=30)
    Physically_Challenged=models.CharField(max_length=30)
    Hobbies=models.CharField(max_length=30)
    Photo=models.CharField(max_length=30)
    Monthly_rate_of_wages=models.CharField(max_length=30,default='')
    Wage_period=models.CharField(max_length=30,default='')
    Payable_days=models.IntegerField(max_length=30,default='')
    #Gross_Wages_Payable_or_Total_Amount=models.CharField(max_length=30,default='')
    Gross_Wages_Payable_or_Total_Amount=models.IntegerField()
    PF_Amount=models.CharField(max_length=30,default='')
    PT_Amount=models.CharField(max_length=30,default='')
    TDS_Amount=models.CharField(max_length=30,default='')
    ADV=models.CharField(max_length=30,default='')
    Net_Salary=models.CharField(max_length=30,default='')


    Address_of_the_principal_Employer=models.CharField(max_length=30,default='')
    Nature_and_Location_of_Work=models.CharField(max_length=30,default='')



    basic=models.CharField(max_length=30, default='')
    dearness_allowances=models.CharField(max_length=30, default='')
    hra=models.CharField(max_length=30, default='')
    conveyance=models.CharField(max_length=30, default='')
    medical_allowance=models.CharField(max_length=30, default='')
    bonus=models.CharField(max_length=30, default='')
    special_allowance=models.CharField(max_length=30, default='')
    Total_deductions=models.CharField(max_length=30, default='')
    Other_allowance=models.CharField(max_length=30, default='')
    overtime_amount=models.CharField(max_length=30, default='')

    esi=models.CharField(max_length=30, default='')
    Net_salary_in_words=models.CharField(max_length=100, default='')

    name_of_contractor=models.CharField(max_length=100, default='')
    address_of_contractor=models.CharField(max_length=200, default='')

    



    def __str__(self):
        return self.Name_of_the_Principal_Employer

class Muster_wages(models.Model):
    SNo=models.CharField(max_length=30, default='')
    Employee_ID=models.CharField(max_length=30, default='')
    Name_of_Workman=models.CharField(max_length=250, default='')
    Father_or_Husband_Name=models.CharField(max_length=250, default='')
    Sex=models.CharField(max_length=30, default='')
    day1=models.CharField(max_length=30, default='')
    day2=models.CharField(max_length=30, default='')
    day3=models.CharField(max_length=30, default='')
    day4=models.CharField(max_length=30, default='')
    day5=models.CharField(max_length=30, default='')
    day6=models.CharField(max_length=30, default='')
    day7=models.CharField(max_length=30, default='')
    day8=models.CharField(max_length=30, default='')
    day9=models.CharField(max_length=30, default='')
    day10=models.CharField(max_length=30, default='')
    day11=models.CharField(max_length=30, default='')
    day12=models.CharField(max_length=30, default='')
    day13=models.CharField(max_length=30, default='')
    day14=models.CharField(max_length=30, default='')
    day15=models.CharField(max_length=30, default='')
    day16=models.CharField(max_length=30, default='')
    day17=models.CharField(max_length=30, default='')
    day18=models.CharField(max_length=30, default='')
    day19=models.CharField(max_length=30, default='')
    day20=models.CharField(max_length=30, default='')
    day21=models.CharField(max_length=30, default='')
    day22=models.CharField(max_length=30, default='')
    day23=models.CharField(max_length=30, default='')
    day24=models.CharField(max_length=30, default='')
    day25=models.CharField(max_length=30, default='')
    day26=models.CharField(max_length=30, default='')
    day27=models.CharField(max_length=30, default='')
    day28=models.CharField(max_length=30, default='')
    day29=models.CharField(max_length=30, default='')
    day30=models.CharField(max_length=30, default='')
    day31=models.CharField(max_length=30, default='')
    working_days=models.CharField(max_length=30, default='')
    week_off=models.CharField(max_length=30, default='')
    hours=models.CharField(max_length=30, default='')
    casual_leaves=models.CharField(max_length=30, default='')
    earned_leaves=models.CharField(max_length=30, default='')
    remarks=models.CharField(max_length=30, default='')
    opening_Leave_Balance=models.CharField(max_length=30, default='')
    No_Eligible_Leaves_added_in_the_month=models.CharField(max_length=30, default='')
    Leaves_taken_in_month=models.CharField(max_length=30, default='')
    closing_leave_balance=models.CharField(max_length=30, default='')
    Total_No_of_Days_in_the_month=models.CharField(max_length=30, default='')
    Total_No_of_Days_Payble=models.CharField(max_length=30, default='')
    unit_of_work_done=models.CharField(max_length=30, default='')
    monthly_rate_of_wages_piece_rate=models.CharField(max_length=30, default='')
    basic=models.CharField(max_length=30, default='')
    dearness_allowances=models.CharField(max_length=30, default='')
    hra=models.CharField(max_length=30, default='')
    conveyance=models.CharField(max_length=30, default='')
    medical_allowance=models.CharField(max_length=30, default='')
    bonus=models.CharField(max_length=30, default='')
    special_allowance=models.CharField(max_length=30, default='')
    basic_earned=models.CharField(max_length=30, default='')
    dearness_allowances_earned=models.CharField(max_length=30)
    hra_earned=models.CharField(max_length=30)
    conveyance=models.CharField(max_length=30)
    medical_allowance_earned=models.CharField(max_length=30, default='')
    bonus_earned=models.CharField(max_length=30, default='')
    special_allowance_earned=models.CharField(max_length=30, default='')
    earned_gross=models.CharField(max_length=30, default='')
    overtime_amount=models.CharField(max_length=30, default='')
    total_amount_earned=models.CharField(max_length=30, default='')
    epf_basic_wages_slab=models.CharField(max_length=30, default='')
    esi=models.CharField(max_length=30, default='')
    epf=models.CharField(max_length=30, default='')
    professional_tax=models.CharField(max_length=30, default='')
    TDS=models.CharField(max_length=30, default='')
    ADV=models.CharField(max_length=30, default='')
    MED=models.CharField(max_length=30, default='')
    total_deduction=models.CharField(max_length=30, default='')
    net_amount_paid=models.CharField(max_length=30, default='')
    time_and_date_of_Payment=models.CharField(max_length=30, default='')
    place_of_payment=models.CharField(max_length=30)
    overtime_dates=models.CharField(max_length=30, default='')
    overtime_Hours=models.CharField(max_length=30, default='')
    total_overtime_hours=models.CharField(max_length=30)
    total_advance=models.CharField(max_length=30, default='')
    advance_date=models.CharField(max_length=30, default='')
    no_of_emi=models.CharField(max_length=30, default='')
    amount_of_emi=models.CharField(max_length=30)
    start=models.CharField(max_length=30, default='')
    end=models.CharField(max_length=30, default='')
    status=models.CharField(max_length=30, default='')
    name_of_employer=models.CharField(max_length=100, default='')
    month=models.CharField(max_length=30, default='')
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.SNo
        
