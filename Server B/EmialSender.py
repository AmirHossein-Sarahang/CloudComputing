import requests


def send_email(e, id):
    temp = "Congratulations!, Your ad was registered with unique number : "
    temp += id
    return requests.post(
        "https://api.mailgun.net/v3/sandboxc93629c668b84ca48c96e3c0431e0faa.mailgun.org/messages",
        auth=("api", "b67fb1a41b7ef718e1b6a487bd46a295-2de3d545-cf7f8e98"),
        data={"from": "mailgun@sandboxc93629c668b84ca48c96e3c0431e0faa.mailgun.org",
              "to": [e],
              "subject": "Advertisement registration",
              "text": temp})
