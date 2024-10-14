# from hugchat import hugchat
# from hugchat.login import Login
# def ai_sorov(refarat_mavzusi):
# # Log in to huggingface and grant authorization to huggingchat
#     EMAIL = "raxmonberdi2004@gmail.com"
#     PASSWD = "Ar1602200408"
#     cookie_path_dir = "./cookies/" # NOTE: trailing slash (/) is required to avoid errors
#     sign = Login(EMAIL, PASSWD)
#     cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

#     # Create your ChatBot
#     chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

#     refarat_mavzusi = "Alisher Navoiy hayoti va ijodi"

#     message_result = chatbot.chat(f"{refarat_mavzusi} - mavzusida maqola yoz") # note: message_result is a generator, the method will return immediately.


#     print(message_result)

from g4f.client import Client

def gpt_sorov(refarat_navzusi):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f" {refarat_navzusi} - mavzusida maqola yoz, maqola uzbek tilida bo'lsn"}],
    )
    javob = response.choices[0].message.content
    return javob

#print(gpt_sorov("Alisher Navoiy"))