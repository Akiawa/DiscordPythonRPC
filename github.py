from pypresence import Presence
import time

client_id = 'your id'
RPC = Presence(client_id)
RPC.connect()

RPC.update(state="state", details ="details",
           large_image="large-image", large_text="Large Text Here!",
           small_image="small-image", small_text="Small Text Here!",
           buttons=[{"label": "", "url": "URL"}])

while True:
    time.sleep(15)