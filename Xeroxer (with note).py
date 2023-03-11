# fd= "F:/NateG";
sd= __import__('os').path.abspath(__file__).replace('\\', '/').split('/');
__iLoc__= len(sd) - 1;
while __iLoc__ > 0:
    if sd[__iLoc__] in ["Dev","Dev-learning"]: break;
    __iLoc__ -= 1;
__workspaceDirectory__= "/".join(sd[:-1]);
__archiveDirectory__= "/".join(sd[:-2]+['(Archives)']+sd[-2:-1]);
__note__= input("$>   ");
dts= __import__('datetime').datetime.now();



ArgV= __import__('sys').argv;
#ThanksTo:
#    DirArchiving-Alg: https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
#    PathProviding-Alg: https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
import os;
import zipfile;
def ArchiveWorkspace(path, ziph):
    for (root,dirs,files) in os.walk(path):
        if(("(Archive)" not in root) and ("jar-out" not in root) and ("artifacts" not in root) and ("(docs)" not in root)):
            for file in files: ziph.write(os.path.join(root,file));
def main(*ArgV):
    # print('archiveLoc','%s/(Archive)/'%__directory__);
    if not os.path.exists(__archiveDirectory__): os.mkdir(__archiveDirectory__);
    time= (dts.utcnow().year, dts.utcnow().month, dts.utcnow().day, dts.utcnow().hour, dts.utcnow().minute, dts.utcnow().second, dts.utcnow().microsecond);
    # print(dts);
    # print('%s/ZipArch (Seconds=%s, tHash=%s, mode=`%s`) --- %s.7z'%(__archiveDirectory__, Secs, hash(dts), ArgV[1], __note__.replace('"', '')), 'w', zipfile.ZIP_DEFLATED);
    __archiveFile__= '%s/ZipArch (time=%s, mode=`%s`) --- %s.7z'%(__archiveDirectory__, time, ArgV[1], __note__.replace('"', ''));
    zipf= zipfile.ZipFile(__archiveFile__, 'w', zipfile.ZIP_DEFLATED);
    ArchiveWorkspace(__workspaceDirectory__, zipf);
    zipf.close();
if __name__=='__main__':
    # print("dir",__archiveDirectory__);
    # print("file",__file__);
    # print(os.getcwd());
    ArgV +=['note'];
    # print(ArgV);
    main(*ArgV);
