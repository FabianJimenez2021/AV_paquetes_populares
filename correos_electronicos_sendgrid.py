import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient



api_key = os.environ.get("SENDGRID_EMAIL")
print(api_key)

mensaje = Mail(
    from_email = ("email"),
    to_emails = ("email"),
    subject = "Correo de prueba",
    html_content= "Curso de <b>Ultimate Python</b>"
)

try:
    api_key = os.environ.get("SENDGRID_API_KEY")
    sg = SendGridAPIClient(api_key)
    respuesta = sg.send(mensaje)
    print(respuesta.status_code,
          respuesta.body,
          respuesta.headers)
except Exception as e:
    print(e)
