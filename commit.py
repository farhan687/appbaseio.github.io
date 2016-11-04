from pygit2 import Signature,Repository
from pygit2.credentials import UserPass
from pygit2.remote import RemoteCallbacks
import netrc
import json
import os
import subprocess
class Repo(object):
  def __init__(self,path,username,password):
    self.repo = Repository(path)
    self.username = username
    self.password = password
    self.path=path

  def commit(self,file,refspec,email,author_username,message):
    self.repo.index.add(file)
    index = self.repo.index
    index.write()
    tree = self.repo.index.write_tree()
    author = Signature(author_username,email)
    self.repo.create_commit(refspec,
        author,
        author,message,tree, [self.repo.head.get_object().hex] )

  def commit_fallback(self,message):
    return subprocess.check_output(["git","commit","-m",message],cwd=self.path)

  def push(self,refspec):
    credentials = UserPass(self.username,self.password)
    remoteCall = RemoteCallbacks(credentials)
    remo = self.repo.remotes["origin"]
    remo.push(refspec,remoteCall)


def getCredentials():
  try:
    MACHINE = os.environ['MACHINE'];
    login = os.environ['LOGIN'];
    password = os.environ['PASSWORD'];

  except:  
    auth = netrc.netrc();
    (login, _, password) = auth.authenticators('api.github.com');
  
  return {'login': login, 'password': password};

credentials = getCredentials();

r = Repo(".",credentials.login, credentials.password)
r.commit("index.html","refs/heads/master","awesome@appbase.io","Appbase bot","Publish master (auto)")

# if the above commit fails, you can try
r.commit_fallback("Commit error")

# then

r.push(["refs/heads/master"]) # here the refspec will be refs/heads/master for master 

