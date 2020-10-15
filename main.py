#w = open("/2ndfile/h.txt") 
import github3
import github3.models

url='https://github.com/skumaryer/'

def authGit(args):
    gh = github3.login(username=skumaryer, password=b3FimCXJHVqGUTwRYpQAfBMR, url='https://github.com/skumaryer/')
    return gh
    w = open('test.txt','r')
    if w >=1:
        print (w.read())
    else:
        print ('no file exists')