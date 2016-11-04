from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.request import Request


# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
    	content = JSONRenderer().render(data)
    	kwargs['content_type'] = 'application/json'
    	super(JSONResponse, self).__init__(content,**kwargs)

@api_view(['GET','POST'])
#@csrf_exempt
def snippet_list(request,format=None):
    if request.method == 'GET':
    	snippets = Snippet.objects.all()
    	serializer = SnippetSerializer(snippets, many=True)
    	#return JSONResponse(serializer.data)
    	return Response(serializer.data)

    elif request.method == 'POST':
    	#data = JSONParser().parse(request)
    	serializer = SnippetSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		#return JSONResponse(serializer.data,status=status.HTTP_201_CREATED)
    		return Response(serializer.data,status=status.HTTP_201_CREATED)
    	return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):
	"""
	Retrieve, update & delete a code snippet
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		#return HttpResponse(status=404)
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		#data = JSONParser().parse(request)
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		#return HttpResponse(status=status.HTTP_204_NO_CONTENT)
		return Response(status=status.HTTP_204_NO_CONTENT)


