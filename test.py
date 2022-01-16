from s2txt import AppAPI as api
from config import Config

import asyncio


async def r():
    # while True:
                # r = await api.s2txt_google(device_index=Config().get("mic"), language=Config().get("lang"), timeout=Config().get("rtimeout"), clear_voice=Config().get("rclear_voice"), phrase_time_limit=Config().get("rphrase_timeout"))
                # print(r)
    r = await api.s2txt_google(device_index=Config().get("mic"), language=Config().get("lang"), timeout=Config().get("rtimeout"), clear_voice=Config().get("rclear_voice"), phrase_time_limit=Config().get("rphrase_timeout"))
    # r = await api.s2txt_vosk(device_index=Config().get("mic"), timeout=Config().get("rtimeout"))
    print(r)

asyncio.run(r())
"""
#print(api.get_device_index("name&index"))
#print(Config().get("lang"))
#a = api.s2txt(8, "uz")
# print(a)
"""
