#coding=utf8
#encoding:utf-8
#当浏览器已安装红杏，可以直接用浏览器下载
import os
import time
  
  
if __name__ == '__main__':
    baseurl = raw_input("请输入批量下载的地址，需包含通配符(*)：".decode('utf-8').encode('gbk'))
    indexStart = int(raw_input("请输入最小的通配符数字：".decode('utf-8').encode('gbk')))
    indexEnd = int(raw_input("请输入最大的通配符数字：".decode('utf-8').encode('gbk')))
    # baseurl = r"http://www-itec.uni-klu.ac.at/ftp/datasets/mmsys12/BigBuckBunny/bunny_2s_480p_only/bunny_2s_100kbit/bunny_2s(*).m4s"
    for index in range(indexStart, indexEnd+1):
        downloadurl = baseurl.replace("(*)",str(index));
        print downloadurl 
        chomeurl = r"C:\Program Files (x86)\Google\Chrome\Application"
        chomeurl = chomeurl.replace("\\","/")
        os.chdir(chomeurl)
        os.system("chrome.exe " + downloadurl)
        time.sleep(1)
        


