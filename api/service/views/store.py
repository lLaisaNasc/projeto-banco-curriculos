from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from common.utils import check_required_fields
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from service.models import Store


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_stores(request):

    stores = Store.objects.all()
    stores_data = []
    for store in stores:
        store_data = {
            'id': store.id,
            'name': store.name,
            'color': store.color
        }
        stores_data.append(store_data)

    return Response(stores_data, status=200)


@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_store(request):

    if not request.user.groups.filter(name='admin').exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    data = request.data

    required_fields = ['name', 'color']

    if not check_required_fields(data, required_fields):
        return Response({"error": "Missing required fields."}, status=400)

    name = data.get('name')
    color = data.get('color')

    store = Store.objects.create(name=name, color=color)

    return Response({"message": "Store creation success."}, status=201)


@api_view(['PUT'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_store(request, id):

    if not request.user.groups.filter(name='admin').exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    data = request.data

    try:
        store = Store.objects.get(id=id)
    except Store.DoesNotExist:
        return Response({"error": "Store not found."}, status=404)

    required_fields = ['name', 'color']

    if not check_required_fields(data, required_fields):
        return Response({"error": "Missing required fields."}, status=400)

    new_name = data.get('name')
    new_color = data.get('color')

    store.name = new_name
    store.color = new_color
    
    store.save()
    return Response({"message": "Store updated successfully."}, status=200)


@api_view(['DELETE'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_store(request, id):

    if not request.user.groups.filter(name='admin').exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    try:
        store = Store.objects.get(id=id)
    except Store.DoesNotExist:
        return Response({"error": "Store not found."}, status=404)

    store.delete()
    return Response({"message": "Store deleted successfully."}, status=200)
