import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5462397690:AAER7IY0DoAGoYMBGLWarfynY1NSEfVa3J4")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "DCBD04")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 18116426)
  API_HASH = os.environ.get("API_HASH", "6f70f07bdfc9b09298396320a4d12847")
  # Sudo users( goto @missrose_Bot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "2063651454").split()))
  SUDO_USERS.append(2063651454)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**ROC Promoter Bot**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/rocx - To get the current settings.\n/rocx no/off/disable - To turn of ROC Promoter bot.\n/rocx {channel username or channel ID} - To turn on and setup the channel.\n/rocx clear - To unmute all members who muted by me.__",
        
       "**Devloped By @Mahmud_Rafi**"
      ]
      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help .\nDeveloped By @AKXVAU"
