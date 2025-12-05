import chainlit as cl
import dotenv

dotenv.load_dotenv

@cl.on_message
async def on_messages(message: cl.Message):
    await cl.Message(content=f"Received: {message.content}").send()