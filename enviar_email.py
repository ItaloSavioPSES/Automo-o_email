import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    corpo_email = """
    <h3>Bot Crazy</h3>
    <p>Fala meu caro amigo, essa mensagem foi enviada por um bot de automoção criado por -SavinhoZein-</p>
    """

    # Configurar a mensagem do e-mail
    msg = MIMEMultipart()
    msg['Subject'] = 'tenebroso'
    msg['From'] = 'email_enviador'
    msg['To'] = 'email_recebedor'
    
    # Adicionar o corpo HTML
    msg.attach(MIMEText(corpo_email, 'html'))

    # Configurações do servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    password = 'ezlypxmqrlyfclub'  # Substitua pela senha de aplicativo

    try:
        # Conectar ao servidor SMTP e enviar o e-mail
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Inicia a conexão TLS
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Chamar a função para enviar o e-mail
enviar_email()
