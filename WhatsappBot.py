from playwright.sync_api import sync_playwright
from time import sleep

grupos = ['o nome dos grupos','outro grupo','outro grupo']

mensagem = ' AQUI VAI A MENSAGEM'

with sync_playwright() as p:

    navegador = p.chromium.launch(channel="chrome",headless=False) #define qual navegador vai usar
    pagina = navegador.new_page() #cria uma pagina vazia 
    link='https://web.whatsapp.com' #designa qual link ira abrir
    pagina.goto(link) #abre o link 
    sleep(42) #tempo para poder ler o qr code
    for i in range(len(grupos)):
        pagina.locator('div[class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp"]').fill(grupos[i]) #coloca o nome do grupo na pesquisa
        sleep(1)
        pagina.get_by_text(grupos[i]).nth(1).click() #clica no nome do grupo pesqusiado
        sleep(1)
        pagina.locator('div[class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"]').fill(mensagem) #coloca a mensagem no campo do envio de texto
        sleep(1)
        pagina.locator('div[class="_2xy_p _3XKXx"]').click() #clica pra enviar a mensagem
        sleep(1)
        pagina.locator('xpath=//*[@id="pane-side"]/div[1]/div/div/div[16]/div/div').click() #clica em outro local, para zerar a pesquisa.
        sleep(1)
    sleep(5)