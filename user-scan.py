
#coding by:trojanx6 

import requests as req
from bs4 import BeautifulSoup as btu



print("\033[92m","""
                                                
@@@  @@@   @@@@@@   @@@@@@@@  @@@@@@@           
@@@  @@@  @@@@@@@   @@@@@@@@  @@@@@@@@          
@@!  @@@  !@@       @@!       @@!  @@@          
!@!  @!@  !@!       !@!       !@!  @!@          
@!@  !@!  !!@@!!    @!!!:!    @!@!!@!           
!@!  !!!   !!@!!!   !!!!!:    !!@!@!            
!!:  !!!       !:!  !!:       !!: :!!           
:!:  !:!      !:!   :!:       :!:  !:!          
::::: ::  :::: ::    :: ::::  ::   :::          
 : :  :   :: : :    : :: ::    :   : :          
                                                
                                                
         @@@@@@@    @@@@@@   @@@@@@@   @@@@@@   
         @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  
         @@!  @@@  @@!  @@@    @@!    @@!  @@@  
         !@!  @!@  !@!  @!@    !@!    !@!  @!@  
         @!@  !@!  @!@!@!@!    @!!    @!@!@!@!  
         !@!  !!!  !!!@!!!!    !!!    !!!@!!!!  
         !!:  !!!  !!:  !!!    !!:    !!:  !!!  
         :!:  !:!  :!:  !:!    :!:    :!:  !:!  
          :::: ::  ::   :::     ::    ::   :::  
         :: :  :    :   : :     :      :   : :  
                                                
""")

class User:
    def __init__(self):
        self.username =  str(input(" [ + ] kullanıcı ismi giriniz: "))
        
        url = f"https://github.com/{self.username}"
        istek = req.get(url)
        soup = btu(istek.content,"lxml")
        ara = soup.find_all(string=[self.username])
        if len(ara) > 0:
            print("\033[91m [ + ] \033[96m GitHub Found:", url)
        elif len(ara) < 1:
            print("\033[91m [ - ] \033[96m Github Not Found: !")      
            
        #Pintestir
        url_1 = f"https://tr.pinterest.com/{self.username}/"
        istek_1 = req.get(url_1)
        soup_1 = btu(istek_1.text,"lxml")
        ara_1 = soup_1.find_all("span",attrs={"class":"tBJ dyH iFc sAJ O2T zDA IZT swG"})
        if len(ara_1) > 0:
            print("\033[91m [ + ] \033[96m Pinsterest Found:", url_1)
        elif len(ara_1) ==  0:
            print("\033[91m [ - ]","\033[96m Pinterest Not Found: !")
           
        #facebook
        url_2 = f"https://m.facebook.com/{self.username}"
        istek_2= req.get(url_2)
        soup_2 = btu(istek_2.text,features="xml")
        ara_2 = soup_2.find_all("div",{"class":"l m"})
        if len(ara_2) > 0:
           print("\033[91m [ + ]","\033[96m Facebook Found:", url_2)
        elif len(ara_2) ==  0:
           print("\033[91m [ - ]","\033[96m Facebook Not Found: !")    
          
          
             
        url_3 = f"https://www.quora.com/profile/{self.username}/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        istek_3 = req.get(url_3,headers=headers)
        html = istek_3.text
        p = html.split()
        if len(p) <= 2000:
            print("\033[91m [ - ]",'\033[96m Quora Not Found: !')
        elif len(p) >= 4584:
            print("\033[91m [ + ]","\033[96m Quora Found:", url_3)
          
        headers = {'User-Agent': 'Mozilla/5.0'}
        url_4 = f"https://www.tiktok.com/@{self.username}"
        istek_4 = req.get(url_4,headers=headers)
        html_4 = istek_4.text
        if len(html_4) < 9294:
           print("\033[91m [ + ]","\033[96m TikTok Found:", url_4)
        elif len(html_4) > 9295:
           print("\033[91m [ - ]",'\033[96m Tiktok Not Found: !')
          
        headers = {'User-Agent': 'Mozilla/5.0'}
        url_5 = f"https://www.reddit.com/user/{self.username}/"
        istek5= req.get(url_5, headers=headers)
        html5= istek5.text
        soup5 = html5.split()
        if len(soup5) == 24135:
           print("\033[91m [ - ]",'\033[96m Reddit Not Found: !')
        elif len(soup5) != 24135:
           print("\033[91m [ + ]",'\033[96m Reddit Found:',url_5)
          
        url6 = f"https://telegram.me/{self.username}"
        istek6 = req.get(url6)
        html6 = istek6.text
        resepsone= html6.split()
        if len(resepsone) == 540:
           print("\033[91m [ - ]",'\033[96m Not Telegram  Found: !')
        elif len(resepsone) != 540:
           print("\033[91m [ + ]",'\033[96m Telegram Found:',url6)
          
          
        url7 = f"https://www.instagram.com/{self.username}/"
        istek7 = req.get(url7)
        html7 = istek7.text
        html7.split()
        if len(html7) < 300000:
            print("\033[91m [ + ] \033[96m Instagram Found:", url7)
        elif len(html7) > 300000:
            print("\033[91m [ - ] \033[96m Instagram Not Found: !")
        
         
if __name__=="__main__":
    User()
