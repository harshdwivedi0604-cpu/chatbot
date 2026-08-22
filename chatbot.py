import random
import gemini
bot= gemini.ConversationAgent()
def get_reply(message):
    message = message.lower()

    reply=bot.ask(message)
    return reply

conversation_log = []

