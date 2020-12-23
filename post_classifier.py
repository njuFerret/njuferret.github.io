import os
import shutil

basePath="_posts"
posts =[f[:-3] for f in os.listdir(basePath) if ".md" in f]
print(posts)
classifiedPath = '分类目录'
if os.path.exists(classifiedPath):
    shutil.rmtree(classifiedPath)
os.mkdir(classifiedPath)

def getBlogPath(filename):
    c = []
    with open(filename,'r',encoding='utf-8') as f:         
        firstLineFound=False
        for l in f.readlines():
            if l.strip().startswith('categories:') and not firstLineFound:
                firstLineFound=True                
                continue
            if firstLineFound:
                if l.strip().startswith('-') :
                    c.append(l.replace('-',"").strip())
                else:
                    break        
    return "/".join(c)


for p in posts:    
    postDir="{}/{}".format(classifiedPath,getBlogPath("{}/{}.md".format(basePath,p)))
    print(p)
    print(postDir)
    if not os.path.exists(postDir):
        os.makedirs(postDir)
    shutil.copy("{}/{}.md".format(basePath,p),"{}/{}.md".format(postDir,p))
    if os.path.exists("{}/{}".format(basePath,p)):
        shutil.copytree("{}/{}".format(basePath,p),"{}/{}".format(postDir,p))