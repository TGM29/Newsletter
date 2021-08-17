from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pywhatkit
browser = webdriver.Chrome()

#Open Links
sites = ['https://tecnoblog.net/','https://g1.globo.com/economia/tecnologia/','https://www.theverge.com/tech','https://www.cnbc.com/technology/','https://www.engadget.com/',"https://www.cnet.com/news/", "https://forbes.com.br/forbes-tech/"]
pages = ['https://g1.globo.com/economia/tecnologia/noticia/2021/08/16/google-e-facebook-anunciam-plano-de-novo-cabo-de-internet-submarino-para-a-asia.ghtml','https://g1.globo.com/economia/agronegocios/agro-a-industria-riqueza-do-brasil/noticia/2021/08/17/de-onde-vem-o-que-eu-uso-cavalos-que-participam-da-producao-do-soro-anti-covid-comem-melaco-e-ate-escutam-musica-classica.ghtml', 'https://g1.globo.com/mg/minas-gerais/noticia/2021/08/17/afegao-que-vive-no-brasil-ha-6-anos-diz-que-esta-preocupado-com-familia-apos-dominio-do-taliba-queremos-paz.ghtml']
browser.maximize_window()



#Abrir links
def abrir_site():
    i = 1
    for site in sites:
        browser.get(site)
        browser.execute_script("window.open()")
        browser.switch_to.window(browser.window_handles[i])
        i = i + 1
    #browser.get("https://translate.google.com/?sl=en&tl=pt&op=translate&hl=pt")

#Get Noticias
def get_news():
    i = 0
    for g in range(1 + len(sites)):
        #Get Window URL
        url = browser.current_url
        write_txt(url)
        #Get head
        #Switch window
        browser.switch_to.window(browser.window_handles[i])
        i = i + 1

#Get Head
def get_head():#Not Working

    title = browser.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[1]/h1')
    print(title)

#Write txt
def write_txt(url):
    news = open("news.txt","a")
    news.writelines(f"\n{url}\n")



#SendWhats
def send_whats():
    news = open("news.txt","r")
    tel_teste = "+5511988110909"
    tel_fernando = "+5511988281642"
    pywhatkit.sendwhatmsg_instantly(tel_teste,news,wait_time= 20)

#Menu
while True:
    x = int(input('''
    1 - Get Sites
    2 - Get News
    3 - Send News
    0 - Exit
    Digite: '''))
    if x == 1:
        abrir_site()
    elif x == 2:
        get_news()
    elif x == 3:
        send_whats()
    elif x == 0:
        break