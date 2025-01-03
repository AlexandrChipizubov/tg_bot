# Telegram bot for financial management (russian language version)
## Instructions for creating your own bot:
  - Install python 3 on your computer (instructions on how to install python: https://phoenixnap.com/kb/how-to-install-python-3-windows )
  - Create your bot in telegram using bot for creating new bots:
    - Insert @BotFather into the telegram search and go to the chat with this bot
    - For detailed information on using this bot, send the command /start
    - To create your personal bot, send the command /newbot
    - Follow the bot's instructions by sending it the information it requests. In the end bot will send you message with information about your bot: link to your bot and token. We will use this token in next steps
  - download the contents of the repository to your computer:
    - click the green "code" button at the top right
    - click "download zip" in the list that opens
  - unzip the downloaded file
  - further instructions explain the sequence of actions in no detail:
    - open unziped folder in IDE (vscode, pycharm, etc.). If you use vscorde, install python extension in vscode.
    - make virtual environment in folder of project
    - activate this virtual environment (.venv\scripts\activate)
    - install library aiogram version 3.15.0 using command pip install
    - make file "config.py" in folder of project. Insert into this file 2 variables:
      TOKEN=' ' and 
      ID=1
    - paste token of your bot into ' '. Save changes.
    - run file "run.py": python run.py. For to run file your virtual environment must be activated.
    - go to the chat with your bot and send command /id. Bot will send you your telegram id.
    - Copy your id and paste into the file "config.py" instead "1". Save changes.
    - stop file run.py: type ctrl+c in terminal and run file again for to apply changes.
    - That's all, you can use your telegram bot sending commands in chat with your bot. For to get list of commands send command /start or /help
