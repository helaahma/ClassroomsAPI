from django.shortcuts import render
from classes.models import Classroom
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .serializers import ListSerializer, CreateSerializer
# Create your views here.

class ClassesList(ListAPIView):

	queryset= Classroom.objects.all()
	serializer_class = ListSerializer

class ClassesDetails(RetrieveAPIView):

	queryset= Classroom.objects.all()
	serializer_class = ListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'

class ClassesCreate(CreateAPIView):

	queryset= Classroom.objects.all()
	serializer_class = CreateSerializer
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user, class_id=self.kwargs['class_id'])


class ClassesUpdate(RetrieveUpdateAPIView):

	queryset= Classroom.objects.all()
	serializer_class = CreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'
	

class ClassesCancel(DestroyAPIView):

	queryset= Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'

