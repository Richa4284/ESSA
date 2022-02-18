from django.db import models
import uuid
from django.core.validators import MinValueValidator

class AbstractBaseModel(models.Model):
    """AbstractBaseModel contains common fields between models.
    All models should extend this class.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Designation(AbstractBaseModel):
    """Designation represents the position a set of employees belongs to."""
    
    designation = models.CharField(max_length=250, null=False)
    
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


     
class Department(AbstractBaseModel):
    """Department represents the sector a set of employees belongs to."""

    name = models.CharField(max_length=250, unique=True, null=False)

    def __str__(self):
        return self.name



class Employee(AbstractBaseModel):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    emp_id = models.AutoField(primary_key=True)
    # id = models.CharField(max_length=10, unique=True, primary_key=True)
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()

    # designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)

    date_of_joining = models.DateField(null=True)

    working_days = models.CharField(max_length=255)
    no_of_leaves = models.IntegerField(null=True)
    
    fixed_annual_ctc = models.CharField(max_length=255,null=True)
    monthly_ctc = models.CharField(max_length=255,null=True) 
    
    balance_leaves = models.CharField(max_length=255,null=True)
    
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.emp_name

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        
        return url


class SalarySlip(AbstractBaseModel):

    employee_code = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    AC_No = models.CharField(max_length=200, primary_key=True, default = 'None')
    pf_number = models.CharField(max_length=255, default = 'None')
     
    basic = models.DecimalField(("Basic & DA"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )

    house_rent_allowance = models.DecimalField(("House Rent Allowance"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )

    misc_allowance = models.DecimalField(("Miscellaneous Allowance"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )

    gross_earnings = models.DecimalField(("Gross Earnings"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    
    #deductions
    provident_fund = models.DecimalField(("Provident Fund"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )
    
    tds_it = models.DecimalField(("TDS/IT"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )

    gross_deductions = models.DecimalField(("Gross Deductions"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )

    # payments
    net_pay = models.DecimalField(("Net Pay"),
        validators=[MinValueValidator(0.00)],
        max_digits=20,
        decimal_places=2,
        default=0.00,
    )

    def save(self):
        """
        Calculate Salary
        :return: None
        """
        total_earnings = (
            self.basic
            + self.house_rent_allowance
            + self.misc_allowance
        
        )
        total_deductions = (
            self.provident_fund + self.tds_it 
        )
        net_pay = total_earnings - total_deductions
        self.gross_earnings = total_earnings
        self.gross_deductions = total_deductions
        self.net_pay = net_pay
        super(SalarySlip, self).save()

    def __str__(self):
        return self.slip_number

     
    
    def netsalary(self): #stored procedure
        return self.Gross_Sal-self.Ded_amt

    def __str__(self):
        return str(self.user)

