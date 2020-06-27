import requests

def main():
    c1 = input("First currency: ")
    c2 = input("Second currency: ")
    res = requests.get("",
    paras = {"base": c1, "symbols": c2})

    #print(res.text)

    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    #status status_code:
    #200 OK
    #201 created
    #400 bad request
    #403 forbidden
    #404 not found
    #405 method not allowed
    #422 unprocessable entity
    data = res.json
    rate = data["rate"][c2]
    print(f"1 {c1} is equal to {rate} {c2}")

if __name__ == '__main__':
    main()
