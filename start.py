from threading import Thread

from bot import main_bot
from scripts import start_script
from send_message import check_message



script = Thread(target=start_script, daemon=True)
message = Thread(target=check_message, daemon=True)

script.start()
message.start()
main_bot()
