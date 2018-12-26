import os
import time
import asyncio

def GetJavaPath():
    flag = False
    paths = os.environ['path'].split(';')
    for path in paths:
        if 'jdk' in path:
            flag = True
            break
    if flag == True:
        return 'OK'
    else:
        return 'NO'

def Get_jar(path):
    jars = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            jars.append((os.path.join(root, name)))

    jars = [file for file in jars if 'jar' in file]
    return jars

async def GetClassInside(filename):
    cmd ="jar.exe -tf %s"%filename 
    classes = os.popen(cmd).read().split('\n')
    return classes

async def fun(filename):
    a = await GetClassInside(filename)

if __name__ == "__main__":
    path = input('pls input path:')
    if path:
        jars = Get_jar(path)
    else:
        jars = Get_jar('.')
        
    time1 = time.time()
    tasks = []
    loop = asyncio.get_event_loop()

    for jar in jars:
        tasks.append(fun(jar))
    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    
    print('解析%d个jar包，耗时%.2fs'%(len(jars),time.time()-time1))
