import requests

Api_key = "WYJor9lKx82SSypwf3bI5PibGbkHoGaDHbtjkSOQ"

def NasaNews(Date):

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)

    params = {'date':str(Date)}

    r = requests.get(Url,params = params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['Url']

    Image_r = requests.get(Image_url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

NasaNews('2020-06-27')