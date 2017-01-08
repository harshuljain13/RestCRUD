from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

# User serializer class to add forward relationship between user and snippets.
#class UserSerializer(serializers.ModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
	#snippets = 	serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
	snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only = True)

	class Meta:
		model=User
		fields = ('id','username','snippets')	

#class SnippetSerializer(serializers.ModelSerializer):
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
	# owner is added so as to relate it with owner in perform_create. also ass owner in fields
	#so as to interact with the model.
	owner  = serializers.ReadOnlyField(source='owner.username')
	#making the relationship between snippet and highlight code link(not highlighted code)
	highlight = serializers.HyperlinkedIdentityField(view_name = 'snippet-highlight', format = 'html')

	class Meta:
		model = Snippet
		fields = ('url','id','highlight','title', 'code', 'linenos', 'language' , 'style', 'owner')

