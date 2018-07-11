import os

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
        

def GetJar():
    files = []
    path = input('请输入jar包所在目录，空缺为当前目录:')
    if path:
        for f in os.listdir(path):
            if 'jar' in f:
                files.append(f)
    else:
        for f in os.listdir():
            if 'jar' in f:
                files.append(f)

    return files

def GetClassInside(filename):
    cmd = "jar.exe -tf %s"%filename 
    classes = os.popen(cmd).read().split('\n')
    return classes

def GetClass(files):
    for f in files:
            classes = GetClassInside(f)
            for c in classes:
                if class_now in c.replace("/", "."):
                    return f

    return 'NO'

if __name__ == '__main__':

    path = GetJavaPath()
    if path == 'NO':
        print('请安装jdk，并将jdk添加至path环境变量')
    else:
        files = GetJar()

        class_now = input('请输入类路径(例:com.asiainfo.appframe.ext.exeframe.remote.client.IClient):')
        if class_now:
    
            f = GetClass(files)
            if f != 'NO':
                print(f)
            else:
                print('Not find!')

            s = input('press enter to continue...')
            if s:
                a = 1

        else:
            print('类路径不能为空')
            s = input('press enter to continue...')
            if s:
                a = 1
