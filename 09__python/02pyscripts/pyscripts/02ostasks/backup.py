import shutil
import datetime
import os


def create__backup(source, destination):
    today = datetime.datetime.today()
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name, "gztar", source)


source = input("Enter the source file make backup: ")
destination = (
    "/home/shaharyar/git-repos/devops-practice/09__python/02pyscripts/pyscripts/ostasks/backups/"
)
create__backup(source, destination)
