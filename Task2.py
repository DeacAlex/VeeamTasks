import time
from datetime import datetime
from dirsync import sync
import sys

period = input("Sync period:")
source_path = "E:/Task2/Source"
dest_path = "E:/Task2/Dest"
log_path = "E:/Task2/logs.csv"
current_timestamp = datetime.now()


class log (object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()

    def flush(self):
        for f in self.files:
            f.flush()


while True:
    f = open(log_path, "a")
    sys.stdout = log(sys.stdout, f)
    sync(source_path, dest_path, 'sync', verbose=True, purge=True, ctime=True)
    time.sleep(int(period))
