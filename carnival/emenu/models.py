from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField()
    logo = models.ImageField(upload_to='vendor_logos', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Vendors'

#create textchoice class for beverages and edibles
class Category(models.TextChoices):
    BEVERAGES = 'Beverages',
    EDIBLES = 'Edibles'

class Menu(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.EDIBLES)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='menu')
    class Meta:
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.vendor.name + ' - ' + self.name
    

class Gallery(models.Model):
    photo = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return f"Photo {self.id}"
    