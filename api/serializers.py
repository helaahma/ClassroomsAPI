from rest_framework import serializers
from classes.models import Classroom

class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model= Classroom
		exclude= ['name']
class CreateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Classroom
		exclude= ['teacher']
