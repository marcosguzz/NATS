import asyncio
import nats

async def main():
    nc = await nats.connect("nats://nats:4222")
    
    sub = await nc.subscribe("as")
    await nc.publish("as", b'Este es un mensaje utilizanddo nats')
    msg = await sub.next_msg()
    msg= str(msg)
    print("Recibido: ", msg)

    await nc.close()

if __name__ == '__main__':
    asyncio.run(main())
