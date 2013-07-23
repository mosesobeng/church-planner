from piston.handler import BaseHandler
from planner.models import Task,Church
from jsonate import jsonate


class CalcHandler( BaseHandler ):
    allowed_methods = ('GET')
    def read( self, request, expression ):
        try:
            tasks = Task.objects.filter(day = request.GET.get('date'),calendar=Church.objects.get(name = request.GET.get('church')) )
            return tasks
        except:
            return {}
