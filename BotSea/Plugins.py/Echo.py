import cs_bot
from cs_bot import MessageSession, logger
from cs_bot.permissions import ANYONE

@cs_bot.on_prefix(["echo"], permission=ANYONE)
def echo(session: MessageSession):
    logger.info(f"Mensagem recebida: {session.message.content}")
    session.send(session.sender.email, session.message.content.lstrip("echo"))
