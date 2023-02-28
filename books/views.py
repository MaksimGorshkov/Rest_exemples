from django.db import IntegrityError
from django.http import JsonResponse
from .models import Books
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Books
from rest_framework import generics
from .serializers import BookSerializer


class BookView (generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


# ##@csrf_exempt
# #def books(request):
# #   if request.method == 'GET':
#         book=Books()
#         book = Books.objects.all().values()
#         return JsonResponse({'books':list(book)})
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')
#         book = Books(title, author, price)
#         try:
#             book.save()
#         except IntegrityError:
#             return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)
#         return JsonResponse(model_to_dict(book), status=200)
