from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from planner.models import Member,Church,Calendar,Task

@csrf_exempt
def home(request):
    if not request.session.__contains__('member'):
        return HttpResponseRedirect('/member-login')
    tasks = Task.objects.filter(day = "2013-07-23" )#today goes here
    t = loader.get_template('index.html')
    c = Context({'tasks': tasks})
    return HttpResponse(t._render(c))
@csrf_exempt
def login(request):
    if request.POST:
        try:
            request.session['member'] = Member.objects.get(username=request.POST['id'],password=request.POST['pword'])
            return HttpResponseRedirect('/planner')
        except Exception:
            t = loader.get_template('login.html')
            c = Context({})
            return HttpResponse(t._render(c))
    t = loader.get_template('login.html')
    c = Context({})
    return HttpResponse(t._render(c))

def logout(request):
    request.session.clear()
    return HttpResponse("logged out")