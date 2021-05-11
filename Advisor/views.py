from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import models
# Create your views here.


class RegisterView(APIView):

    def post(self, request):
        userame = request.data['userame']
        email = request.data['email']
        password = request.data['password']

        user = models.User(userame=userame, email=email, password=password)
        if user.varify():
            if not user.isExist():
                user.save()
                token = RefreshToken.for_user(user)
                return JsonResponse({'refresh': str(token),'access': str(token.access_token), "user-id":user.id}, status=200)        

            return HttpResponse(status=400)
        
        return HttpResponse(status=400)


# @csrf_exempt
# def all_advisors(request):
#     if request.method=='POST':
#         name = request.POST['name']
#         image_url = request.POST['image_url']
#         advisor = models.Advisor(name=name, image_url=image_url)
#         if advisor.varify():
#             advisor.save()
#             return HttpResponse(status=200)
        
#         return HttpResponse(status=400)
#     return HttpResponse(status=400)





class AdvisorView(APIView):
    
    def post(self, request):
        name = request.data['name']
        image_url = request.data['image_url']

        advisor = models.Advisor(name=name, image_url=image_url)
        if advisor.varify():
            advisor.save()
            return HttpResponse(status=200)
        
        return HttpResponse(status=400)

class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        if email=='' or password=='':
            return HttpResponse(status=400)

        user = models.User.objects.filter(email=email).first()

        if user is None:
            return HttpResponse(status=401)
        
        if not user.check_password(password):
            return HttpResponse(status=401)
        

        token = RefreshToken.for_user(user)
        
        return JsonResponse({
            "refresh":str(token),
            "access": str(token.access_token),
            "user-id": user.id,
        }, status = 200)

        return JsonResponse({'refresh': str(token),
                'access': str(token.access_token), "user-id":user.id}, status=200)


class allAdvisorView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, userid):
        advisors = models.Advisor.objects.all()
        advisors_list = []
        for advisor in advisors:
            advisors_list.append({
                "Name": advisor.name,
                "Profile Url":advisor.image_url,
                "Advisor Id":advisor.id
            })
        
        return JsonResponse({"Advisors": advisors_list}, status=200)


class bookView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, userid, advisorid):
        time = request.data["time"]

        if time=='':
            return HttpResponse(status=400)
        
        book = models.Booking(advisor_id=advisorid, booking_time=time)
        book.save()
        return HttpResponse(status=200)

class ScheduleView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, userid):
        bookings = models.Booking.objects.all()

        schedule_list = []
        for booking in bookings:
            advisor = models.Advisor.objects.filter(id=booking.advisor_id).first()

            schedule_list.append({
                "Advisor Name": advisor.name,
                "Profile Url":advisor.image_url,
                "Advisor Id":advisor.id,
                "Booking Time":booking.booking_time,
                "Booking Id":booking.id
            })
        
        return JsonResponse({"Schedule": schedule_list}, status=200)