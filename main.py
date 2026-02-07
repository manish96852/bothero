import asyncio
from pyrogram import idle
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.handlers import RawUpdateHandler
from pyrogram.raw import types

from functions import CHAT_ID, app

# Track VC participants
vc_participants = set()


async def handle_raw_updates(client, update, users, chats):
    """Handle raw updates to detect VC joins"""
    try:
        # Check if it's a group call participant update
        if isinstance(update, types.UpdateGroupCallParticipants):
            # Get the chat/group ID from the call
            call_id = update.call.id
            
            # Process each participant
            for participant in update.participants:
                user_id = None
                
                # Get user ID from different peer types
                if isinstance(participant.peer, types.PeerUser):
                    user_id = participant.peer.user_id
                elif isinstance(participant.peer, types.PeerChat):
                    user_id = participant.peer.chat_id
                elif isinstance(participant.peer, types.PeerChannel):
                    user_id = participant.peer.channel_id
                
                if user_id:
                    # Check if user joined (not muted and not left)
                    if not participant.left and not participant.muted:
                        # Check if this is a new participant
                        if user_id not in vc_participants:
                            vc_participants.add(user_id)
                            
                            # Get user info
                            try:
                                user = await app.get_users(user_id)
                                user_name = user.first_name
                                if user.last_name:
                                    user_name += f" {user.last_name}"
                                
                                # Send message to group
                                await app.send_message(
                                    CHAT_ID,
                                    f"🎤 **{user_name}** joined the voice chat!"
                                )
                            except Exception as e:
                                print(f"Error getting user info: {e}")
                    
                    # Remove from tracking if left
                    elif participant.left and user_id in vc_participants:
                        vc_participants.discard(user_id)
                        
    except Exception as e:
        print(f"Error in raw update handler: {e}")


@app.on_message(filters.command("start") & filters.chat(CHAT_ID))
async def start_command(_, message: Message):
    await message.reply_text(
        "✅ **Bot is active!**\n\n"
        "I will notify when someone joins the voice chat."
    )


async def main():
    # Add raw update handler for VC events
    app.add_handler(RawUpdateHandler(handle_raw_updates))
    
    await app.start()
    print("✅ Bot started! Monitoring voice chat joins...")
    await idle()


if __name__ == "__main__":
    asyncio.run(main())
