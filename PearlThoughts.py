from http import client
import slack
import os
from pathlib import Path
from dotenv import load_dotenv

#Setting Env Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['TOKEN'])


client.chat_postMessage(channel='#general', text='I Am Online')
