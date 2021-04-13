from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,RegexValidator
# Create your models here.




class Profile(models.Model):
    name=models.CharField(max_length=100)
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    age=models.IntegerField(default=18,validators=[MinValueValidator(18)])
    address=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=20,default="female",choices=(("male","male"),("female","female"),("other","other")))
    status=models.CharField(max_length=20,default="single",choices=(("single","single"),("married","married"),("seperated","seperated"),("commited","commited")))
    contact=models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=11,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    pic=models.ImageField(default='default.png',upload_to="images")

    def __str__(self):
        return "%s" % self.user

class Post(models.Model):
    pic=models.ImageField(upload_to="images",null=True)
    subject=models.CharField(max_length=200)
    msg=models.TextField(null=True,blank=True)
    cr_date=models.DateField(auto_now_add=True)
    uploaded_by=models.ForeignKey(to=Profile,on_delete=models.CASCADE,null=True,related_name="post_profile")

    def __str__(self):
        return "%s" % self.subject



class Comment(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE,null=True,related_name="comments")
    commented_by=models.ForeignKey(to=Profile,on_delete=models.CASCADE,null=True)
    msg=models.TextField()
    cr_date=models.DateField(auto_now_add=True)
    flag=models.CharField(max_length=20,null=True,blank=True,choices=(("Racist","Racist"),("Abusive","Abusive")))

    def __str__(self):
        return "%s" % self.msg

class PostLike(models.Model):
    post=models.ForeignKey(to=Post,on_delete=models.CASCADE)
    liked_by=models.ForeignKey(to=Profile,on_delete=models.CASCADE)
    cr_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.liked_by

class FollowUser(models.Model):
    profile=models.ForeignKey(to=Profile,on_delete=models.CASCADE,related_name="profile")
    followed_by=models.ForeignKey(to=Profile,on_delete=models.CASCADE,related_name="followed_by")

    def __str__(self):
        return "%s is followed by %s" % (self.profile,self.followed_by)
