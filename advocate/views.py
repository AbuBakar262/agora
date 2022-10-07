from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, pagination
from advocate.models import Advocate, Company
from advocate.serializers import CreateAdvocateSerializer, CreateCompanySerializer, ListAdvocateSerializer, \
    ListCompanySerializer


class DynamicPagination(pagination.PageNumberPagination):
    page_size = 10


class AdvocateViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Advocate.objects.all()
    serializer_class = CreateAdvocateSerializer
    pagination_class = DynamicPagination

    def create_advocate(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors,
                    "data": ""
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                "status": True,
                "message": "Advocate User Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "status": False,
                "message": e.args[0],
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)

    def list_advocate(self, request, *args, **kwargs):
        try:
            id = self.kwargs.get('pk')
            advocate = Advocate.objects.get(id=id)
            serializer = ListAdvocateSerializer(advocate)
            return Response({
                "status": True,
                "message": "Advocate User Fetched Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": False,
                "message": e.args[0],
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all()
    serializer_class = CreateCompanySerializer

    def create_company(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors,
                    "data": ""
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                "status": True,
                "message": "Company Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "status": False,
                "message": e.args[0],
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)

    def list_company(self, request, *args, **kwargs):
        try:
            id = self.kwargs.get('pk')
            companies = Company.objects.get(id=id)
            serializer = ListCompanySerializer(companies)
            return Response({
                "status": True,
                "message": "Companies Listed Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": False,
                "message": e.args[0],
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)