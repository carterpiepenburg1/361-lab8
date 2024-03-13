from email._header_value_parser import Section

from django.shortcuts import render
from django.views import View
from datetime import datetime
from ticketLog.models import Sections, Days, Ticket


# Create your views here.
class Home(View):
    def get(self, request):
        print(Days.choices)
        return render(request, "home.html", {"days": Days.choices, "sections": Sections.choices})

    def post(self, request):
        print(Days.choices)
        # convert datetime-local string to a Python datetime
        date = datetime.strptime(request.POST['dateTime'], '%Y-%m-%dT%H:%M')  # replace the first argument
        # instantiate and save a Ticket
        ticket = Ticket(dateTime=date, section=request.POST['section'], dayOfWeek=date.strftime("%A"))
        ticket.save()
        # render a response, identical to the page rendered by get
        return render(request, "home.html", {"days": Days.choices, "sections": Sections.choices})


class History(View):
    def get(self, request):
        return render(request, "history.html", {"days": Days.choices, "sections": Sections.choices})

    def post(self, request):
        # extract day and section from POST
        day = Days(request.POST['day']).name
        section = request.POST['section']
        # query (filter) for tickets
        filtered = Ticket.objects.filter(dayOfWeek=day, section=section)
        # render a response (with a table of matching tickets)
        return render(request, "history.html", {"days": Days.choices, "sections": Sections.choices, "filtered": filtered})
