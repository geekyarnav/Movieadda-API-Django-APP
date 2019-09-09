from django.shortcuts import render
from django.http import HttpResponse
#FROM DJANGO.VIEWS PACKAGE WE IMPORT CLASS CALLED VIEWS FOR USING FULL FUNCTIONALITY IN OUR CLASS
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#class based views
class Another(View):
    
    books = Book.objects.all()
    # books = Book.objects.filter(is_published="True")
    # books = Book.objects.get(id=2) SKIP LOOP PART IT DOESNT WORK
    
    output = " " 
    
    for book in books:
        # print(f"We have {len(books)} Books in our DB")    
        output = output +f"We have this book name \t {book.title} with the Book ID: \t {book.id}<br>"



    def get(self,request):
        # here SELF is accesing object in this class like in javascript this.props
        return HttpResponse(self.output)

# viewset class-helps to give all the https methods and work on them
# Modelviewset is give proper ui for our model data 

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer         

    # queryset
    queryset = Book.objects.all()  

    # TOKEN AUTHENTICATION 
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (IsAuthenticated)






#function based views
# def function(request):
#     # return HttpResponse"FBV"
#     books = Book.objects.all()
#     return render(request,'1.html',{'books':books})





