import base64
import pprint
from github import Github
import os

GIT_TOKEN = "8e3a35b91b03c77cfbd2e5d787a28c4998560861"

def createDirectoryStructure(mypath):
    # create game directory structure from mypath
    os.makedirs(mypath, 0o777, exist_ok=True)

## MAIN ##

# base directory
basename = "GAMEPARTITION"

# get our current directory
currentdir = os.getcwd()

# buildout our new structure - main branch
ourdir = os.path.join(currentdir, basename, '_igm')
createDirectoryStructure(ourdir)

# next branch
dirname = os.path.join(ourdir, '_igm')
createDirectoryStructure(dirname)

# library is next
libname = os.path.join(ourdir, 'Library')
createDirectoryStructure(libname)

# slots
slotsname = os.path.join(libname,'slots')
createDirectoryStructure(slotsname)

# create several gamenames
gamelist = ['gamenameA', 'gamenameB', 'gamenameC']
for glist in gamelist:
    subdir = os.path.join(slotsname, glist)
    createDirectoryStructure(subdir)

# fetch some gits
git = Github(GIT_TOKEN)
repo = git.get_repo('martan3d/rpiwebapp')
file_content = repo.get_contents('main.py')
file_data = base64.b64decode(file_content.content)

destination = os.path.join(slotsname, gamelist[0], 'main.py')

f = open(destination,"w")
f.write(str(file_data))
f.close()
