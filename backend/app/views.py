from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth.password_validation import validate_password
from .serializers import UserSerializer
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_user(request):
    if request.method == 'POST':
        user_data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'first_name': request.data.get('Firstname'),
            'last_name': request.data.get('Lastname'),
        }
        try:
            username = request.data.get('username')
            if User.objects.filter(username=username).count():
                error_message = f'Username "{username}" is already in use.'
                return JsonResponse({"error": [error_message]},
                                    status=status.HTTP_409_CONFLICT
                                    )
            password = request.data.get('password')
            try:
                validate_password(password)
            except ValidationError as e:
                errors = f'Password not valid. Please try a strong password "{str(e)}"'
                return JsonResponse({"error": [errors]}, status=status.HTTP_406_NOT_ACCEPTABLE)
            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
            else:
                errs = {
                    "error": [f"{k}:{str(v[0] if v is not None and type(v) == list and len(v) > 0 else '')}" for k, v in
                              serializer.errors.items()]}
                return Response(errs, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': f'User creation failed: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)