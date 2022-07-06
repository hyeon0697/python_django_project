from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product

from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):

    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"},status=405)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):   ##필요한 필드를 나오게하는 usage
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invaild": "Not Good Data"}, status=400)