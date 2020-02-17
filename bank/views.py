from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from bank.serializers import detailsAPI
from bank.models import BankDetails
from django.http import HttpResponse, JsonResponse


def bank(request):
    if "ifsc" in request.GET:
        data=request.GET['ifsc']
        try:
            queryset=BankDetails.objects.get(ifsc=data)
            qp=detailsAPI(queryset)
            return JsonResponse(qp.data, safe=False)
        except Exception as e:
            queryset={
                "Error" : "resource not found"
            }
            return JsonResponse(queryset)
    #if  "city" and "name" in request.GET:
    elif request.GET.get('city') and request.GET.get('name'):
        bname=request.GET['name'].upper()
        bcity=request.GET['city'].upper()
        queryset=BankDetails.objects.filter(city=bcity,bank_name=bname)

        if queryset.count()<1:
            qp={"Error": "resource not found"}
            return JsonResponse(qp)
        else:
            qp=detailsAPI(queryset,many=True)
            return JsonResponse(qp.data,safe=False)
    else:
        error={
            "Error": "Sorry this method not allow"
        }

        return JsonResponse(error)

def home(request):
    return render(request,"index.html")