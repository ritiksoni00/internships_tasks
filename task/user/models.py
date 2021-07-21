from django.db import models



class User(models.Model):
    first_name  = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    username = models.CharField(max_length=10)

    def __str__(self) :
        return str(self.username)


# i am unable to understand how to create model level relationship rather than the simple one! sorry!

class Post(models.Model):
    user = models.CharField(max_length=10)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fk = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return str(self.user)