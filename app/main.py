# =====================================================================
'''
Update Covid 19 (Real Time tiap Per-Jam)
Sumber Data : Kawalcorona.com (Ethical Hacker Indonesia)
Dev         : Sulistiawan A P (Mazwan98 on Github)
...
'''
# =====================================================================


from plyer import notification          # pip install plyer
import requests                         # pip install requests
from bs4 import BeautifulSoup           # pip install bs4
import time


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"sulteng.ico",
        timeout = 10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        # notifyMe("Halo Satgas Sulteng !", "Mari kita hentikan penyebaran virus ini bersama-sama !\n\nDev : Sulistiawan | Kominfo Sulteng\nSource : Kawalcorona.com")
        notifyMe("Halo Satgas Sulteng !", "Update C-19 / Jam\n\nDev : Sulistiawan | Kominfo Sulteng\nSource : Kawalcorona.com")

        sumberData = getData('https://kawalcorona.com/')
        soup = BeautifulSoup(sumberData, 'html.parser')

        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            
            # print(tr.get_text()) #cuma tak pakek nge-Debug sj
            myDataStr += tr.get_text()
            
        itemList = myDataStr.split("\n\n")
        myDataStr = myDataStr[1:]


        lokasi = ['Sulawesi Tengah']        
        for item in itemList[0:]:
            
            data = item.split('\n')
            if data[1] in lokasi:           
                nJudul = f'Kasus Covid-19 di {data[1]}'         
                nTeks = f"Positif\t:\t{data[2]}\nSembuh\t:\t{data[3]}\nWafat\t:\t{data[4]}"
                notifyMe(nJudul, nTeks)

                time.sleep(2) # Detik
        time.sleep(3600) # Sett Durasi Per Jam