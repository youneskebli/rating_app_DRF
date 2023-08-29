from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=15,default="",blank=False)
    description=models.TextField(max_length=300,default="",blank=False)
    
    def nbr_of_rating(self):
        rating = Rating.objects.filter(phone=self)
        return len(rating)
    def avr_of_rating(self):
        sum = 0
        rating = Rating.objects.filter(phone=self)
        for x in rating:
            sum += x.stars
            if (len(rating) > 0 ):
                return sum/len(rating)
            else:
                return 0
        
    def __str__(self):
        return self.name
    
class Rating(models.Model):
    phone = models.ForeignKey(Phone,related_name="ratings",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="ratings",on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    class Meta:
        unique_together = (('phone','user'),)
        index_together = (('phone','user'),)

        
       