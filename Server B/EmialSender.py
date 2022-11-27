import requests

# b67fb1a41b7ef718e1b6a487bd46a295-2de3d545-cf7f8e98
# mailgun@sandboxc93629c668b84ca48c96e3c0431e0faa.mailgun.org
def send_email(e, id, t):
    try:
        return requests.post(
            "https://api.mailgun.net/v3/sandboxc93629c668b84ca48c96e3c0431e0faa.mailgun.org/messages",
            auth=("api", ""),
            data={"from": "",
                  "to": [e],
                  "subject": "Advertisement registration",
                  "text": message(t, id)})
    except():
        print("Error in Send Emial!")

def message(t,i):
    temp = ""
    if t:
        temp = "Congratulations!, Your ad was registered with unique number : "
        temp += i
        return temp
    else:
        temp = "Your ad is rejected!"
        return temp
