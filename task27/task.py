import psutil
import sched, time
def ram_cpu():
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):

        cpu_percentage = psutil.cpu_percent()
        ram_percentage = psutil.virtual_memory()._asdict()['percent']
        print('percentages of:',cpu_percentage,ram_percentage)
        s.enter(5, 1, do_something, (sc,))
    s.enter(5, 1, do_something, (s,))
    s.run()
ram_cpu()
