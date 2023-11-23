
import asyncio
import aiocoap
from aiocoap import resource, Context, Message

async def handle_coap(request):
    payload = b"Hello, CoAP!"
    return Message(payload=payload, code=aiocoap.numbers.codes.CONTENT)

async def main():
    try:
        # Create CoAP server context
        root = resource.Site()
        root.add_resource(['hello'], handle_coap)
        
        # Use '::1' for IPv6 loopback address
        context = await Context.create_server_context(root, bind=('::1', 5683))

        print("CoAP server is running.")
        
        # Run the server indefinitely
        await asyncio.Event().wait()

    except Exception as e:
        print(f"Error in CoAP server: {e}")

if __name__ == "__main__":
    asyncio.run(main())
