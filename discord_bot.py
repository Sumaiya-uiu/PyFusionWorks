from discord.ext import commands, tasks
import discord

# Replace with your text channel ID
CHANNEL_ID = 1275181438291152988
NOHUP_FILE_PATH = "/home/ubuntu/sales-navigator-scripts/nohup.out"  # Update this path if necessary

intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    send_tail_output.start()

@tasks.loop(minutes=30)
async def send_tail_output():
    try:
        # Fetch the channel by ID (text channel in this case)
        channel = await bot.fetch_channel(CHANNEL_ID)

        if isinstance(channel, discord.TextChannel):
            # Send the last 5 lines of the file to the text channel
            with open(NOHUP_FILE_PATH, 'r') as f:
                lines = f.readlines()[-5:]
            await channel.send("```" + "".join(lines) + "```")
        else:
            print(f"Error: Channel with ID {CHANNEL_ID} is not a text channel.")
    except discord.NotFound:
        print(f"Error: Could not find channel with ID {CHANNEL_ID}")
    except discord.Forbidden:
        print(f"Error: Bot does not have permission to send messages in channel with ID {CHANNEL_ID}")
    except Exception as e:
        print(f"Error: {e}")

# Make sure to replace 'YOUR_BOT_TOKEN' with your bot token
bot.run('DISCORD_BOT_TOKEN')
