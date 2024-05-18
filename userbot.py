
import asyncio
import json
import os
import re

from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    """Checks if a string represents a boolean value (on/off, true/false, etc.)

    Args:
        value: The string value to check.
        default: The default value to return if the input is not a boolean.

    Returns:
        True if the value represents "on", "true", "yes", etc., False if it represents
        "off", "false", "no", etc., otherwise returns the default value.
    """

API_ID = int(os.environ.get('API_ID'))  # Assuming API_ID is an integer environment variable
API_HASH = os.environ.get('API_HASH')  # Assuming API_HASH is a string environment variable
SESSION = os.environ.get('SESSION')  # Assuming SESSION is a string environment variable, likely a session name

SUDO = [6511724381, 1867106198]  # List of authorized user IDs

async def main():
    """Asynchronous main function to run the Telegram bot."""

    global piro  # Declare piro globally to avoid potential scoping issues

    piro = Client(
        "Gojo",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="user")  # Assuming user-defined plugins are in the "user" directory
    )

    print("Your session started")

    # Add your bot logic here, using piro for Telegram interactions
    # ... (your bot code using piro.on_message, piro.send_message, etc.)


if __name__ == '__main__':
    asyncio.run(main())
    piro.run()
