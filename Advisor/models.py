from django.db import models

# Create your models here.

class User(models.Model):
    userame = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def isExist(self):
        if User.objects.filter(userame = self.userame):
           return True

        return False 


    def data(self):
        return {"userame":self.userame, "email":self.email, "password":self.password}

    def check_password(self, password):
        if password==self.password:
            return True
        
        return False

    def varify(self):
        if self.userame=='' or self.email=='' or self.password=='':
            return False
        return True


class Advisor(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=10000)

    
    def varify(self):
        if self.name=='' or self.image_url=='':
            return False
        return True

class Booking(models.Model):
    advisor_id = models.IntegerField()
    booking_time = models.CharField(max_length=100)





# class Advisors(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     name = models.CharField(max_length=200)
#     image_url = models.CharField(max_length=200)

#     def data(self):
#         return {"name":self.name, "image_url":self.image_url}

# class registerUser(models.Model):
#     id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
#     username = models.CharField(max_length=200, unique=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)

#     def isExist(self):
#         if registerUser.objects.filter(username = self.username):
#            return True

#         return False 

#     def data(self):
#         return {"username":self.username, "email":self.email, "password":self.password}

#     def check_password(self, password):
#         if password==self.password:
#             return True
        
#         return False
