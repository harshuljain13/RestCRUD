from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# User serializer class to add forward relationship between user and snippets.
class UserSerializer(serializers.ModelSerializer):
	snippets = 	serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

	class Meta:
		model=User
		fields = ('id','username','snippets')	

class SnippetSerializer(serializers.ModelSerializer):
	# owner is added so as to relate it with owner in perform_create. also ass owner in fields
	#so as to interact with the model.
	owner  = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Snippet
		fields = ('id','title', 'code', 'linenos', 'language' , 'style', 'owner')

