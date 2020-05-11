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


import requests, sys, os, string, random
dir = os.path.dirname(os.path.abspath(sys.argv[0]))


def gen_loader_name(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

file_name = gen_loader_name()


def init():
    if len(sys.argv) == 1:
        print("  No arguments were given")
        exit(-1)
        
    get_loader(sys.argv[1])


def get_loader(s_cookie):
    aw_sess = requests.Session()
    cookie = requests.cookies.RequestsCookieJar()
    
    cookie.set('mybbuser', s_cookie)
    
    aw_sess.cookies = cookie
    get_bytes = aw_sess.get('https://aimware.net/forum/panel.php?action=download-client-v5' )
    loader = get_bytes.content
    
    save(loader)


def save(file):
    with open('{}\\{}.exe'.format(dir, file_name), 'wb') as aw_loader:
        aw_loader.write(file)
        aw_loader.close()


if __name__ == "__main__":    
    init()
