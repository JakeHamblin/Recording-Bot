import discord
from pytz import timezone
from datetime import datetime
from config import *

# Create bot instance
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

# Set timezone
eastern = timezone('US/Eastern')

# Create slash command group
recording = bot.create_group(name="recording", description="Commands related to controlling the recording bot", guild_ids=[Config.guild])

# Create list of connections
connections = {}

# When bot is started
@bot.event
async def on_ready():
    # Print login message (useful for Pterodactyl)
    print(f"We have logged in as {bot.user}")

    # Set bot status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="time"), status='online')

# Clock in command
@recording.command(guild_ids=[Config.guild], description="Start recording")
async def start(ctx):
    channel = ctx.author.voice

    time = datetime.now(eastern)

    if channel is None:
        await ctx.respond("You're not in a voice chat", ephemeral=True)
    else:
        voice = await channel.channel.connect()
        connections.update({ctx.guild.id: {"voice": voice, "recording": True}})

        file_name = ctx.author.display_name + "-" + ctx.author.discriminator + "-" + time.strftime('%m/%d/%Y')

        voice.start_recording(
            discord.sinks.MP3Sink(),
            once_done,
            ctx.author,
            file_name
        )

        await ctx.respond("Recording has started", ephemeral=True)

async def once_done(sink, member: discord.Member, name: str, *args):
    await sink.vc.disconnect()
    time = datetime.now(eastern)
    files = [discord.File(audio.file, f"{name}.{sink.encoding}") for user_id, audio in sink.audio_data.items()]
    channel = bot.get_channel(Config.log_channel)

    embed = await embed_builder("Recording Saved", "")
    embed.add_field(name="Started by", value=member.mention, inline=False)
    embed.add_field(name="Saved At", value=time.strftime('%m/%d/%Y - %I:%M:%S %p') + " EST", inline=False)
    await channel.send(embed=embed)
    await channel.send(files=files)

@recording.command(guild_ids=[Config.guild], description="Pause recording")
async def pause(ctx):
    if ctx.guild.id in connections:
        vc = connections[ctx.guild.id]["voice"]

        if connections[ctx.guild.id]["recording"] == True:
            vc.toggle_pause()
            connections[ctx.guild.id]["recording"] = False
            await ctx.respond("I've paused the recording", ephemeral=True)
        else:
            vc.toggle_pause()
            connections[ctx.guild.id]["recording"] = True
            await ctx.respond("I've unpaused the recording", ephemeral=True)
    else:
        await ctx.respond("I'm not currently recording", ephemeral=True)

@recording.command(guild_ids=[Config.guild], description="Stop recording")
async def stop(ctx):
    if ctx.guild.id in connections:
        vc = connections[ctx.guild.id]["voice"]
        vc.stop_recording()
        del connections[ctx.guild.id]
        await ctx.respond("The audio has been saved and logged", ephemeral=True)
    else:
        await ctx.respond("I'm not currently recording", ephemeral=True)

# Function for building embeds
async def embed_builder(title, description):
    # Create embed
    embed = discord.Embed(title=title, description=description, color=discord.Color.from_rgb(255, 0, 0))

    return embed

bot.run(Config.token)