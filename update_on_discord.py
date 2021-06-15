from bs4 import BeautifulSoup as bs
import requests
from time import sleep
import datetime
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}
x = datetime.datetime.now()
hour = x.hour
minute = x.minute
date_1= x.day
month = x.month
year = x.year
date_time1 = f'{date_1}-{month}-{year} at {hour}:{minute}'


from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(
    url='https://discordapp.com/api/webhooks/852078898531663893/6Lh_exi9UYdNHWeqv05XtFMODBE0jc7JOOpoeXhF-QzpqIEtEsLI_KfsIL0E2v6q87R0', username="GLOSAVY- LIST OF LOANS, UPDATE!!")


while True:
    print('still running..')
    try:
        r = requests.get('https://gosavy.com/lt/paskolu-sarasas',headers = headers)
        soup  = bs(r.content,'html.parser')
        trs = soup.find('table').find('tbody').findAll('tr')

        for tr in trs:
            tds = tr.findAll('td')
            try:
                annual_interest = float(tds[3].text.replace('%',''))
                last_percen = float(tds[8].text.replace('%',''))
                link = tds[-1].find('a')['href']
                link = f'https://gosavy.com/{link}'


                if last_percen<100 and annual_interest>20:
                    embed = DiscordEmbed(title='UPDATE!', description=f"We Found One That Meets The Criteria.\n\nAnnual Interest Rate: {annual_interest}%\nLast Percentage: {last_percen}% \n Time: {date_time1}\n Here is the link: {link}")
                    webhook.add_embed(embed)
                    response = webhook.execute()
                    webhook.remove_embeds()
                    print('bot sent files')
            except:
                pass
    except:
        embed = DiscordEmbed(title='Something Wrong!', description=f"This could be the sites problem. \nCheck if the website is working on your browser.\nOr contact Your Developer(sorowerhossan01-fiverr)")
        webhook.add_embed(embed)
        response = webhook.execute()
        webhook.remove_embeds()
        print('need your help, sorower')
    sleep(30)