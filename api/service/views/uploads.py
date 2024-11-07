from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from service.models import Foto

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upload_foto(request):

    foto_file = request.FILES.get('foto')

    if not foto_file:
        return Response({"error": "No image file provided."}, status=400)

    foto = Foto.objects.create(foto=foto_file)

    return Response({"message": "Image upload successfully.", "id": foto.id, "foto_url":foto.foto.url}, status=201)


@api_view(['DELETE'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_foto(request, id):
    try:
        foto = Foto.objects.get(id=id)

    except Foto.DoesNotExist:
        return Response({"error": "Foto not found."}, status=404)

    foto.delete()
    return Response({"message": "Foto deleted successfully."}, status=200)
