'''
       __                     __                                __  __        __    __  __     ______    ______   _______    ______
      /  |                   /  |                              /  |/  |      /  |  /  |/  |   /      \  /      \ /       |  /      \
  ____$$ |  ______   ______  $$ |   __   ______   __   __   __ $$/ $$ |  ____$$ | _$$ |$$ |_ /$$$$$$  |/$$$$$$  |$$$$$$$/  /$$$$$$  |
 /    $$ | /      \ /      \ $$ |  /  | /      \ /  | /  | /  |/  |$$ | /    $$ |/ $$  $$   |$$____$$ |$$ \__$$ |$$ |____  $$ ___$$ |
/$$$$$$$ |/$$$$$$  |$$$$$$  |$$ |_/$$/ /$$$$$$  |$$ | $$ | $$ |$$ |$$ |/$$$$$$$ |$$$$$$$$$$/  /    $$/ $$    $$< $$      \   /   $$<
$$ |  $$ |$$ |  $$/ /    $$ |$$   $$<  $$    $$ |$$ | $$ | $$ |$$ |$$ |$$ |  $$ |/ $$  $$   |/$$$$$$/   $$$$$$  |$$$$$$$  | _$$$$$  |
$$ \__$$ |$$ |     /$$$$$$$ |$$$$$$  \ $$$$$$$$/ $$ \_$$ \_$$ |$$ |$$ |$$ \__$$ |$$$$$$$$$$/ $$ |_____ $$ \__$$ |/  \__$$ |/  \__$$ |
$$    $$ |$$ |     $$    $$ |$$ | $$  |$$       |$$   $$   $$/ $$ |$$ |$$    $$ |  $$ |$$ |  $$       |$$    $$/ $$    $$/ $$    $$/
 $$$$$$$/ $$/       $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$/$$$$/  $$/ $$/  $$$$$$$/   $$/ $$/   $$$$$$$$/  $$$$$$/   $$$$$$/   $$$$$$/


'''

'''
 *
 * Title: Aimware Loader Downloader
 * Author: drakewild#2853
 * Description: Downloads Aimware Loader
 *
'''


import requests, sys, os, string, random, json, ctypes, msvcrt
from time import sleep
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
clear = lambda: os.system('cls')

def gen_loader_name(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

file_name = gen_loader_name()


def init():
    ctypes.windll.kernel32.SetConsoleTitleW("AIMWARE.NET DOWNLOADER")
    os.system('mode con: cols=70 lines=20')



def menu():
    for args in sys.argv:
        if args == "update":
            update_cookie()
    if file_exist(dir+'\\cookie.aw'):
        pass
    else:
        update_cookie()

    with open(dir+"\\cookie.aw", 'r') as c:
        cookie = c.read()
        c.close()
    get_loader(cookie)




def update_cookie():
    clear()
    print("  Cookie not found!")
    sleep(2)
    clear()
    print("")
    print("--------------------------AIMWARE DOWNLOADER--------------------------")
    print("")
    print("                    <1> Edit a cookie")
    print("                    <2> Back")
    wh = msvcrt.getch().decode("utf-8").lower()

    if wh == "1":
        with open(dir+'\\cookie.aw', 'w') as c_file:
            print("")
            cookie = input(" Paste a cookie: ")
            c_file.write(cookie)
            c_file.close()
        menu()
    elif wh == "2":
        menu()
    else:
        print(" Wrong option!")
        sleep(2)
        update_cookie()



def get_loader(s_cookie):
    aw_sess = requests.Session()
    cookie = requests.cookies.RequestsCookieJar()
    cookie.set('mybbuser', s_cookie)
    aw_sess.cookies = cookie
    try:
        get_bytes = aw_sess.get('https://aimware.net/forum/panel.php?action=download-client-v5' )
        loader = get_bytes.content
    except Exception as error:
        print(" An error occured! {}".format(error))
        sleep(10)
        exit(-1)

    save(loader)


def save(file):
    with open('{}\\{}.exe'.format(dir, file_name), 'wb') as aw_loader:
        aw_loader.write(file)
        aw_loader.close()
    run('{}\\{}.exe'.format(dir, file_name))


def run(loader):
    os.startfile(loader)
    exit(-1)

def file_exist(f_name):
    return True if os.path.isfile(f_name) else False


if __name__ == "__main__":
    init()
    menu()
