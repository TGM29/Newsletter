from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

#Open Links
sites = ['https://tecnoblog.net/','https://g1.globo.com/economia/tecnologia/','https://www.theverge.com/tech','https://www.cnbc.com/technology/','https://gadgets.ndtv.com/news',"https://www.cnet.com/news/"]
pages = ['https://g1.globo.com/economia/tecnologia/noticia/2021/08/16/google-e-facebook-anunciam-plano-de-novo-cabo-de-internet-submarino-para-a-asia.ghtml','https://g1.globo.com/economia/agronegocios/agro-a-industria-riqueza-do-brasil/noticia/2021/08/17/de-onde-vem-o-que-eu-uso-cavalos-que-participam-da-producao-do-soro-anti-covid-comem-melaco-e-ate-escutam-musica-classica.ghtml', 'https://g1.globo.com/mg/minas-gerais/noticia/2021/08/17/afegao-que-vive-no-brasil-ha-6-anos-diz-que-esta-preocupado-com-familia-apos-dominio-do-taliba-queremos-paz.ghtml']
browser.maximize_window()
#Abrir links
def abrir_site():
    i = 1
    for site in pages:
        browser.get(site)
        browser.execute_script("window.open()")
        browser.switch_to.window(browser.window_handles[i])
        i = i + 1
    #browser.get("https://translate.google.com/?sl=en&tl=pt&op=translate&hl=pt")

#Get Noticias
def get_news():
    i = 0
    for g in range(1 + len(pages)):
        #Get Window URL
        url = browser.current_url
        print(url)
        #Get head
        #Switch window
        browser.switch_to.window(browser.window_handles[i])
        i = i + 1


def get_head():

    title = browser.find_element_by_xpath('/html/body/div[2]/main/div[2]/div[1]/h1')
    print(title)



#Menu
while True:
    x = int(input('''
    1 - Get Sites
    2 - Get News
    0 - Exit
    Digite: '''))
    if x == 1:
        abrir_site()
    elif x == 2:
        get_news()
    elif x == 0:
        break