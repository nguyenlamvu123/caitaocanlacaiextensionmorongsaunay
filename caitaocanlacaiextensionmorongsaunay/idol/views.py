from django.shortcuts import render
from django.template import loader
from .models import Idol
from .forms import IdolSearchForm

# Create your views here.
def idol_index(request): 
   if 'name' in request.GET:
      name = request.GET['name']
      idols = Idol.objects.filter(name__contains=name)
   else:
      name = 'Name'
      idols = Idol.objects.all()
   
   form = IdolSearchForm(initial={'name': name})
   idols = Idol.objects.all()
   #template = loader.get_template('index.html')
   context = {
      'idols': idols,
      'form' : form,
            }
   #return HttpResponse(template.render(context, request))
   return render(request, 'index.html', context)
