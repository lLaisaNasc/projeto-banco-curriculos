from rest_framework.decorators import api_view, parser_classes, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from common.utils import check_required_fields
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from service.models import Department


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_departments(request):

    departments = Department.objects.all()
    departments_data = []
    for department in departments:
        department_data = {
            'id': department.id,
            'name': department.name,
            'color': department.color,
        }
        departments_data.append(department_data)

    return Response(departments_data, status=200)


@api_view(['POST'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_department(request):

    if not request.user.groups.filter(name='admin').exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    data = request.data

    required_fields = ['name', 'color']

    if not check_required_fields(data, required_fields):
        return Response({"error": "Missing required fields."}, status=400)

    name = data.get('name')
    color = data.get('color')

    department = Department.objects.create(name=name, color=color)

    return Response({"message": "Department creation success."}, status=201)


@api_view(['PUT'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_department(request, id):

    if not request.user.groups.filter(name='admin').exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    data = request.data

    try:
        department = Department.objects.get(id=id)
    except Department.DoesNotExist:
        return Response({"error": "Department not found."}, status=404)

    required_fields = ['name', 'color']

    if not check_required_fields(data, required_fields):
        return Response({"error": "Missing required fields."}, status=400)

    new_name = data.get('name')
    new_color = data.get('color')

    department.name = new_name
    department.color = new_color
    
    department.save()
    return Response({"message": "Department updated successfully."}, status=200)


@api_view(['DELETE'])
@parser_classes([JSONParser])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_department(request, id):

    if not request.user.groups.filter(name='admin').exists():
        return Response({"error": "You do not have permission to perform this action."}, status=403)

    try:
        department = Department.objects.get(id=id)
    except Department.DoesNotExist:
        return Response({"error": "Department not found."}, status=404)

    department.delete()
    return Response({"message": "Department deleted successfully."}, status=200)
