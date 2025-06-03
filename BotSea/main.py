import os
from dotenv import load_dotenv
import cs_bot
from cs_bot import StartupConfig
from cs_bot.adapters import sop_bot

load_dotenv()

config = {
    "adapter": {
        "app_id": os.getenv("APP_ID"),
        "app_secret": os.getenv("APP_SECRET"),
        "signing_secret": os.getenv("SIGNING_SECRET")
    },
    "callback_path": os.getenv("CALLBACK_PATH", "/callback")
}

cs_bot.init(StartupConfig.parse_obj(config))
cs_bot.register_adapter(sop_bot.Adapter)
cs_bot.load_plugin("plugins.echo")

if __name__ == "__main__":
    cs_bot.run(host="0.0.0.0", port=8000)
