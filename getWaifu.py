import requests
import shutil
import random


# Retrieves a random waifu from the server.
def getWaifu():
    num = random.randint(0, 100000)
    imgName = 'example-{}.jpg'.format(num)
    # https://www.thiswaifudoesnotexist.net/snippet-59984.txt
    introName = 'snippet-{}.txt'.format(num)

    url = 'https://www.thiswaifudoesnotexist.net/{}'.format(imgName)
    introUrl = 'https://www.thiswaifudoesnotexist.net/{}'.format(introName)

    # Act like a regular user so we don't get blocked ;)
    params = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, params, stream=True)

    # save the raw bytes from the response as the image.
    with open(imgName, 'wb') as fOut:
        shutil.copyfileobj(response.raw, fOut)
    
    response = requests.get(introUrl, params, stream=True)

    # save the raw bytes from the response as the image.
    with open(introName, 'wb') as fOut:
        shutil.copyfileobj(response.raw, fOut)


for waifu in range(10):
    getWaifu()
