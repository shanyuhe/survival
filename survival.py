# 环境python3
import argparse
import time

import requests
import threading
i = -1
urls_txt = []
name_txt = ''
header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

def logo():
    print("\033[91m[+] Author\033[0m    : 一秋小叶")
    print("\033[91m[+] Email\033[0m     : 2900180755@qq.com")
    print("\033[91m[+] Github\033[0m    : https://github.com/shanyuhe")
    time.sleep(3)

def url_list(txt):
    global name_txt
    global urls_txt
    name_txt =  "200_"+txt
    with open(txt, mode='r',encoding='utf-8') as fp:
        urls_txt = fp.readlines()

def return_url():
    global i
    i += 1
    url = urls_txt[i].replace('\n', '').replace('\r', '')
    return url

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        while True:
            try:
                crawler(return_url(),self.name)
            except:
                break
        print("Thread exit: " + self.name)


# 定义功能函数，访问固定url地址
def crawler(url_t,ts):
    url_ = url_t.replace('\n', '').replace('\r', '')
    try:
        http_i = url_t.find("http")
        if http_i == -1:
            try:
                url = 'http://'+url_
                req = requests.get(url, headers=header, timeout=20).status_code
                if req < 100000:
                    print(name_txt)
                    with open(name_txt, mode='a') as fp3:
                        fp3.write(url + '\n')
                        print(f'{ts} ==> {url} ==> {req}')
            except Exception as e:
                try:
                    url = 'https://' + url_
                    req = requests.get(url, headers=header, timeout=20).status_code
                    if req < 100000:
                        with open(name_txt, mode='a') as fp3:
                            fp3.write(url + '\n')
                            print(f'{ts} ==> {url} ==> {req}')
                except Exception as e:
                    try:
                        url = 'http://www.' + url_
                        req = requests.get(url, headers=header, timeout=20).status_code
                        if req < 100000:
                            with open(name_txt, mode='a') as fp3:
                                fp3.write(url + '\n')
                                print(f'{ts} ==> {url} ==> {req}')
                    except Exception as e:
                        try:
                            url = 'https://www.' + url_
                            req = requests.get(url, headers=header, timeout=20).status_code
                            if req < 100000:
                                with open(name_txt, mode='a') as fp3:
                                    fp3.write(url + '\n')
                                    print(f'{ts} ==> {url} ==> {req}')
                        except Exception as e:
                            print(f'{ts} ==> {url} ==> Error')


        else: # 带协议的url
            req = requests.get(url_, headers=header, timeout=20).status_code
            if req < 100000:
                with open(name_txt, mode='a') as fp3:
                    fp3.write(url_ + '\n')
                    print(f'{ts} ==> {url_} ==> {req}')
    except Exception as e:
        print(f'{ts} ==> {url_} ==> Error')



# 创建线程列表
def goRun(txt,T):
    threads = []
    url_list(txt)
    # 开启线程数量
    print(f'Starting Thread  + {str(T)}')
    for i in range(int(T)):
        # 给每个线程命名
        ts ="Thread-"+str(i)
        thread = myThread(ts)
        thread.start()
        # 将线程添加到线程列表
        threads.append(thread)

    # 等待所有线程完成
    for t in threads:
        t.join()
if __name__ == '__main__':
    logo()

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help='txt文件位置')
    parser.add_argument('-t', help='线程数量')

    args = parser.parse_args()
    if (args.r) and (args.t):
        goRun(args.r, args.t)



