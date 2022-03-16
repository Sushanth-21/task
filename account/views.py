from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import OTP
from random import randint
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user(request):
    try:
        if request.user.is_superuser:
            request.data['password'] = ''.join(
                [str(randint(0, 9)) for i in range(8)])
            ser = RegisterSerializer(data=request.data)
            ser.is_valid(raise_exception=True)
            user = ser.save()
            return Response({'username': user.username, 'password': request.data['password']}, status=HTTP_201_CREATED)
        return Response({'message': "You do not have permission to perform this action."}, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_student(request):
    try:
        if request.user.is_staff:
            request.data['password'] = ''.join(
                [str(randint(0, 9)) for i in range(8)])
            request.data['is_staff'] = False
            request.data['is_superuser'] = False
            ser = RegisterSerializer(data=request.data)
            ser.is_valid(raise_exception=True)
            user = ser.save()
            return Response({'username': user.username, 'password': request.data['password']}, status=HTTP_201_CREATED)
        return Response({'message': "You do not have permission to perform this action."}, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    try:
        user = User.objects.get(username=request.data['username'])
        flag = True
        while flag:
            try:
                code = ''.join([str(randint(0, 9)) for i in range(6)])
                otp = OTP.objects.create(user=user, code=code)
                flag = False
            except:
                continue
        return Response({'code': otp.code, 'message': 'Enter code sent to {}'.format(user.email)}, status=HTTP_200_OK)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    try:
        user = User.objects.get(username=request.data['username'])
        otp = OTP.objects.get(user=user)
        if otp.code == request.data['code']:
            if request.data['new_password'] != request.data['confirm_password']:
                return Response({'message': 'passwords do not match'}, status=HTTP_400_BAD_REQUEST)
            user.set_password(request.data['new_password'])
            user.save()
            otp.delete()
            return Response({'message': 'password change successful'}, status=HTTP_200_OK)
        return Response({'message': 'codes do not match'}, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    try:
        if request.user.is_superuser:
            users = User.objects.all()
            data = []
            for u in users:
                data.append(UserSerializer(u).data)
            return Response(data, status=HTTP_200_OK)
        return Response({'message': "You do not have permission to perform this action."}, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_students(request):
    try:
        print(request.user.is_staff)
        if request.user.is_staff:
            users = User.objects.all().filter(is_staff=False, is_superuser=False)
            data = []
            for u in users:
                data.append(UserSerializer(u).data)
            return Response(data, status=HTTP_200_OK)
        return Response({'message': "You do not have permission to perform this action."}, status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    try:
        profile = UserSerializer(request.user).data
        return Response(profile, status=HTTP_200_OK)
    except Exception as e:
        return Response({'message': str(e)}, status=HTTP_400_BAD_REQUEST)
