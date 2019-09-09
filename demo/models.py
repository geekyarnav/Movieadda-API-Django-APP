from django.db import models

# Create your models here.
# ONE TO ONE - 2 records folowing 1-1 relationship 'extention for one model'
class BookNumber(models.Model):
    Isbn_10 = models.CharField(max_length=10,blank=True)
    Isbn_13 = models.CharField(max_length=13,blank=True)

class Book(models.Model):

    #one to one field link with BookNumber   
    # number = models.OneToOneField(BookNumber, null=True,blank =True, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=36,
                            blank=False,    
                            unique=True)    
                            # default='', 
                            # choices=CONDITIONS
    description =models.TextField(max_length=200,blank=True) 
    price = models.DecimalField(default=0,max_digits=3,decimal_places=2)
                                                       
    published_date=models.DateTimeField(blank=True,null=True,default=None)
                                # auto_now=True,auto_now_add=True
    is_published =models.BooleanField(default=False)                            
    cover = models.ImageField(upload_to="covers/",blank=True)
                            #  fileField 
                            # height and width also set 
    
                                                        

    def __str__(self):
        return self.title

