import git
import shutil
from datetime import datetime


source = '/home/rushi/devops/bash'
dest = './config'

shutil.copytree(source, dest)

# Git Automation

repo = git.Repo("./")
repo.git.add(A=True)
commit_message=f"Auto backup: {datetime.now()}"
repo.index.commit(commit_message)
origin = repo.remote(name='origin')
origin.push()

print("✅ Backup & push completed.")


