import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_NUMERO")
cliente = Client(sid, token)
mensaje = cliente.messages.create(
    body = "Hola hola",
    from_= numero,
    to="+56956476534"
)