import concurrent.futures
import os
import requests
from requests.exceptions import Timeout

import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



Good = open("Good.txt", "a")
Bad = open("Bad.txt", "a")
Time_out = open("Time_out.txt", "w")
exception = open("Exception.txt", "w")


class colors:
  LGREEN = '\033[38;2;129;199;116m'
  LBLUE = '\033[38;5;111m'
  LRED = '\033[38;2;239;83;80m'
  LPURPLE = '\033[38;2;148;73;209m'
  RESET = '\u001B[0m'
  LXC = '\033[38;2;255;152;0m'
  GREY = '\033[38;2;158;158;158m'
  LYELLOW = '\033[38;2;255;255;0m'
  LLIME = '\033[38;2;0;255;0m'



ip_file = "b.txt"
with open(ip_file, "r") as url:
  url2 = url.readlines()
URL = url2

proxy = {
    'http': 'http://root:root@198.23.137.251:11236',
    #'http': 'http://root:root@66.135.30.124:38633',
    #'http': 'http://root:root@154.17.12.106:17868',
    #'https': 'https://root:root@154.17.12.106:17868',
    #'http': 'http://ohxqlmfa:txxtblnwv860@38.154.227.167:5868',
}


def Marzban(url3):

  """
  #display()
  #print(f"{colors.GREY}=> {colors.RESET} {colors.LYELLOW} {url3}")"""

  
  try:
    for a in range(0,10):
      for b in range(0,10):
        for c in range(0,10):
          for d in range(0,10):

              url4 = f"https://{url3}/wizpanel1{a}{b}{c}{d}/login.php".strip()
              # Send the request
              with requests.get(url4, timeout=30,  proxies=proxy, verify=false) as response:
                status_code = response.status_code
                if status_code == 200 :
                  print(f"{colors.GREY}=> {colors.RESET} {colors.LGREEN} successful : {url3}{colors.RESET} ")
                  Good.write(f"{url4}")
                  Good.flush()
                else :
                  print(f"{colors.GREY}=>  failed : {url3} {status_code}{colors.RESET} ")
  except Exception as e:
    print(f"{colors.LPURPLE}=>  Exception : {url3} {e} {colors.RESET} ")
    exception.write(f"{url3} : {e}\n")
    exception.flush()
        
  finally:
    print(f"{colors.GREY}=> {colors.RESET} {colors.LRED} Failed : {url3} {colors.RESET} ")
    Bad.write(url3)
    Bad.flush()  
    
def main():

  with concurrent.futures.ThreadPoolExecutor(
      max_workers=200) as executor:  #Adjust max_workers as needed
    executor.map(Marzban,url2)


if __name__ == "__main__":
  main()
