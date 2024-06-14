from django.db import models

# Create your models here.

class Footwears(models.Model):
    product_options=(
        ('sandals','sandals'),
        ('slipperandflipflops','slipperandflipflops'),
        ('casualshoes','casualshoes'),
        ('specialcollections','specialcollections'),
        ('flatshoes','flatshoes'),
        ('schooledition','schooledition'),
    )
    product_category=models.CharField(max_length=100,choices=product_options)
    types=(
        ('ladies','ladies'),
        ('gents','gents'),
        ('boys','boys'),
        ('girls','girls'),
        ('kids','kids')
    )
    product_types=models.CharField(max_length=100,choices=types)
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.product_name
    
class Footwearimages(models.Model):
    product=models.ForeignKey(Footwears,on_delete=models.CASCADE)
    colors=(
        ('Black','Black'),
        ('Blue','Blue'),
        ('Brown','Brown'),
        ('Camel','Camel'),
        ('Cherry','Cherry'),
        ('Gold','Gold'),
        ('Grape','Grape'),
        ('Green','Green'),
        ('Grey','Grey'),
        ('Maroon','Maroon'),
        ('Mehandi','Mehandi'),
        ('Navy','Navy'),
        ('Olive','Olive'),
        ('Peach','Peach'),
        ('Peacock','Peacock'),
        ('Pink','Pink'),
        ('Purple','Purple'),
        ('Tan','Tan'),
        ('Violet','Violet'),
        ('White','White'),
        ('Wine','Wine'),
        ('Yellow','Yellow'),
    )
    product_color=models.CharField(max_length=100,choices=colors)
    product_image=models.ImageField(upload_to='imagesall/',null=True,blank=True)

