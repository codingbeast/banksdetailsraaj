from django.db import models
#bankDetails model for store banks details data into sqllite database
class BankDetails(models.Model):
    ifsc = models.CharField(max_length=50)
    bank_id=models.CharField(max_length=20)
    branch=models.CharField(max_length=70)
    address=models.TextField()
    city=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    state=models.CharField(max_length=200)
    bank_name=models.TextField()
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
