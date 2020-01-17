from django.shortcuts import render
from .models import cpu_ram_model
import psutil
from django.core import serializers
import sched, time
from django.http import HttpResponse
def ram_cpu():
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        cpu_percentage = psutil.cpu_percent()
        ram_percentage = psutil.virtual_memory()._asdict()['percent']
        data_to_save=cpu_ram_model(cpu_percentage=cpu_percentage,ram_percentage=ram_percentage)
        data_to_save.save()
        # data=cpu_ram_model.objects.save(update_fields=[cpu_percentage, ram_percentage])
        # datadisplay=cpu_ram_model.objects.all()
        # print(datadisplay)
        print('percentages of:',cpu_percentage,ram_percentage)
        s.enter(5, 1, do_something, (sc,))
    s.enter(5, 1, do_something, (s,))
    s.run()
# ram_cpu()

def get_ram_cpu(request):
    datadisplay = cpu_ram_model.objects.all()
    print(datadisplay)
    # assuming obj is a model instance
    # serialized_obj = serializers.serialize('json', [datadisplay, ])
    return HttpResponse(datadisplay)


# ram_cpu()
def display_data(request):
    data=cpu_ram_model.objects.all()
    return render(request,'home.html',{'data':data})