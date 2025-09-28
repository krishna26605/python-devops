import os
import shutil
import datetime



def takes_backup(source,destination):
    today=datetime.date.today()
    file_path=os.path.join(destination , f"backup_{today}")
    shutil.make_archive(file_path , "gztar" , source)

source= "/mnt/c/Users/Krishna/OneDrive/Desktop/s3-python"
destination= "/mnt/c/Users/Krishna/OneDrive/Desktop/s3-python/backed_up"


takes_backup(source,destination)
