import os
import time
import threading

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

def GetClassInside(filename,class_path):
    global flag
    cmd = "jar -tf %s"%filename 
    classes = os.popen(cmd).read().split('\n')
    for c in classes:
        if class_path in c.replace('/','.'):
            filename = filename.split("\\")
            flag = filename[-1]
            return 0
    



if __name__ == "__main__":
    time1 = time.time()
    path = input('pls input path:')
    if path:
        jars = Get_jar(path)
    else:
        jars = Get_jar('.')

    class_path = input('pls input class_path')
    threads = []
    for jar in jars:
        # classes = GetClassInside(jar)
        t = threading.Thread(target=GetClassInside, args=(jar,class_path))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    
    print('解析%d个jar包，耗时%.2fs，结果如上'%(len(threads),time.time()-time1))

