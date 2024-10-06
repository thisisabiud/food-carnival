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


class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.vendor.name + ' - ' + self.name
    