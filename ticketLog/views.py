from django.shortcuts import render
from django.views import View
from datetime import datetime
from ticketLog.models import Sections, Days, Ticket
# Create your views here.
class Home(View):
    def get(self,request):
        print(Days.choices)
        return render(request,"home.html",{"days":Days.choices,"sections":Sections.choices})

    def post(self,request):
        print(Days.choices)
        #extract form data from POST
        #convert datetime-local string to a Python datetime
        datetime.strptime('2015-01-02T00:00', '%Y-%m-%dT%H:%M')
        #instantiate and save a Ticket
        #render a response, identical to the page rendered by get
        return render(request,"home.html",{"days":Days.choices,"sections":Sections.choices})

class History(View):
    def get(self,request):
        return render(request,"history.html",{"days":Days.choices,"sections":Sections.choices})

    def post(self,request):
    #extract day and section from POST
    #query (filter) for tickets
        Ticket.objects.filter(dayOfWeek="U").values()
    #render a response (with a table of matching tickets)
        return render(request,"history.html",{"days":Days.choices,"sections":Sections.choices})
