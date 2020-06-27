import requests

def main():
    res = requests.get("http://www.google.com/")
    print(res.text)

if __name__ == '__main__':
    main()
