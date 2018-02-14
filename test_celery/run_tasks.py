#from .tasks import longtime_add
import time
from github import Github

import os.path as osp 



if __name__ == '__main__':
    
  #  repo_dir = osp.join(rw_dir, 'my-new-repo')
    
    
    
    GITHUB_USER = 'GennaroCipolletta'
    GITHUB_PASSWORD = 'gheroghers1'
    REPO = 'GennaroCipolletta/Prova_Emage'

    ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues' % REPO
    AUTH = (GITHUB_USER, GITHUB_PASSWORD)
    g = Github(GITHUB_USER,GITHUB_PASSWORD)
    for repo in g.get_user().get_repos():
           print(repo.name)

    import subprocess
    subprocess.call(["git", "pull"])
    subprocess.call(["make"])
    subprocess.call(["make", "test"])
    
    # rividere il codice per prelevare il codice e fare la build..o make
    # ricordarsi che abbiamo 2 repositories
    #file='/Desktop/VirtualEnv/ProvaCelery_Emage1/pythonenv'
    #repo_dir=osp.join(osp.dirname(__file__), 'config.ini')
    #file_name = osp.join(repo_dir, 'new-file')

    r = git.Repo.init(repo_dir)
        # This function just creates an empty file ...
    open(file_name, 'wb').close()
    r.index.add([file_name])
    r.index.commit("initial commit")
    #result = longtime_add.delay(1,2)
    # at this time, our task is not finished, so it will return False
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
