import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19638390"))
    API_HASH = os.environ.get("API_HASH", "ff2861aa26b33c0bead7ec26ab30e04f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5561908781:AAEJFOFf6fpSJeqxWOaakHFvH8dfPCHX9oo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCrwVAGh-BTPQMchyn1T4f69Bw3m7hphuBKs0uI6GM0Rk380GpL9W1z2PhLew8c7dRdY2bTg_4GfgPOEJPAmY-gsW5NF8v1sk7qfivFqk_cXuXBmCJ2ICF3kZ1HRyOCdnpWvbjn5nkJtT0SkY500bSpccPU2aBUO9UenBqdjZYdAaEmXrjMug3YE-FAdqQ-c9lRerqlXbfZXNvK-ETUE8DO1_6SB9HYDTT7NDJYv5dG5fqc_AmWO9RUIePgfhrW9otqKlDBcVWtbWA4ZlG8Zd0xVzU7-NqzltrKTFQFUgqd6xkisEtkzA32fPj_BIAuvT-I7mjU0cGdxGovAoPZHTDEAAAAAVI7FzsA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Darkdevil2music_bot")
    SUPPORT = os.environ.get("SUPPORT", "Darkdevilbots") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "Darkdevilbots") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/5ee2d173f37a407efd863.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/5ee2d173f37a407efd863.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5674571579")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
