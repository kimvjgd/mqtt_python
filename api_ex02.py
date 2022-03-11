from requests import get

def download(url, file_name):
  with open(file_name, "wb") as file:
    response = get(url)
    file.write(response.content)
  
if __name__ == '__main__':
  url = "https://www.delftstack.com/img/Python/image%20example.jpg"
  # download(url, "arduino.png")
  download(url, url.split('/')[-1])

# https://www.delftstack.com/img/Python/image%20example.jpg