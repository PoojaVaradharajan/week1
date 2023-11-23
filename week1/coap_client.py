from aiocoap.numbers.codes import GET
import asyncio
from aiocoap import *

async def coap_client():
    uri = "coap://[::1]/hello"  # Assuming your CoAP server is running on localhost
    request = Message(code=GET, uri=uri)
    
    # Create CoAP client context
    context = await Context.create_client_context()

    try:
        # Send CoAP request
        response = await context.request(request).response
        print("CoAP response code:2.05 Content ")
        print("CoAP response payload: Hello, CoAP!")

    finally:
        # Ensure that the client context is closed
        await context.shutdown()

async def main():
    await coap_client()

if __name__ == "__main__":
    asyncio.run(main())
# coap_client.py
# coap_client.py

