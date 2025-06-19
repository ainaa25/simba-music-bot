import asyncio
from pyrogram import idle
from simba import simba

async def main():
    await simba.start()
    print("✅ Simba Music Bot sedang berjalan!")
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
