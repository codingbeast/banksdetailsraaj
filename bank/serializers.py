from bank.models import BankDetails
from rest_framework import serializers

#modelserializer use for json response
class detailsAPI(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields=('ifsc','bank_id','branch','address','city','district','state','bank_name')