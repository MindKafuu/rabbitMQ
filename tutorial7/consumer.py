import asyncio
import logging

import aio_pika

async def main() -> None:
    # logging.basicConfig(level=logging.DEBUG)
    connection = await aio_pika.connect_robust(
        'amqp://guest:guest@10.131.200.163:5672/'
    )

    queue_name = "test_queue"

    async with connection:
        channel = await connection.channel()

        await channel.set_qos(prefetch_count=10)

        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)
                    print("Done.")

                    if queue.name in message.body.decode():
                        break

if __name__ == "__main__":
    asyncio.run(main())