import os
import subprocess
import time
from datetime import datetime
import psutil

filename = 'E:/VeeamTasks/task1_log.txt'
header = 'Date CPU_usage Mem_consum No_open_handles\n'
path = input("Insert the path to the file:")
interval_time = int(input("Please introduce the data collection time interval:"))
p = subprocess.Popen([path],
                     bufsize=-1,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     stdin=subprocess.PIPE)


def cpu_percent_psutil():
    process = psutil.Process(os.getpid())
    cpu = process.cpu_percent(interval=1)
    return cpu


def mem_consumption_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_percent()
    return mem


def get_open_files():
    process = psutil.Process(os.getpid())
    open_files = process.open_files()
    return len(open_files)


def check_process_running(path):
    for proc in psutil.process_iter():
        if path.lower() in proc.name().lower():
            return True


def log_data():
    with open(filename, 'a') as log:

        log.write(date_time + str(cpu_percent_psutil()) + ';' + str(mem_consumption_psutil()) + ';' + str(get_open_files())+'\n')
        time.sleep(interval_time)


def WriteHeader(filename, header):
    file = open(filename, 'r')
    lines = [line for line in file]
    file.close()
    if lines and lines[0] == header:
        return True
    else:
        file = open(filename, 'w')
        file.write(header + ''.join([line for line in lines if not line == header]))
        file.close()
        return True


if __name__ == '__main__':
    while True:
        if check_process_running(path) is True:
            if WriteHeader(filename, header):
                now = datetime.now()
                date_time = now.strftime("%d-%m-%Y %H:%M:%S: ")
                file = open(filename, 'a')
                file.write('{}:{};{};{}\n'.format(date_time,cpu_percent_psutil(),mem_consumption_psutil(),get_open_files()))
                file.close()
        else:
            exit()
