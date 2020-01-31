##from django.shortcuts import render
##import openpyxl
##
##
##def index(request):
##    if "GET" == request.method:
##        return render(request, 'myapp/index.html', {})
##    else:
##        excel_file = request.FILES["excel_file"]
##
##        # you may put validations here to check extension or file size
##
##        wb = openpyxl.load_workbook(excel_file)
##
##        # getting a particular sheet by name out of many sheets
##        worksheet = wb["Sheet1"]
##        print(worksheet)
##
##        excel_data = list()
##        # iterating over the rows and
##        # getting value from each cell in row
##        for row in worksheet.iter_rows():
##            row_data = list()
##            for cell in row:
##                row_data.append(str(cell.value))
##            excel_data.append(row_data)
##
##        return render(request, 'myapp/index.html', {"excel_data":excel_data})

from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import dictionary as City

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(Eng__icontains=query) | Q(Viet__icontains=query) | Q(pronunciation__icontains=query)
        )
        return object_list
####object_list, the default name for the context object ListView returns

####html
##<ul>
##  {% for city in object_list %}
##    <li>
##      {{ city.name }}, {{ city.state }}
##    </li>
##  {% endfor %}
##</ul>
####html
