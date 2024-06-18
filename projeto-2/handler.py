import json
import boto3

sessao = boto3.Session(profile_name='automacao-curso', region_name='us-east-1')
cliente_s3 = sessao.client('s3')
cliente_ses = sessao.client('ses')


def envio_email(event, context):
    resultado = cliente_s3.get_object(
        Bucket='send-email-ses-projeto2',
        Key='usuarios.csv'
    )

    dados = resultado['Body'].readlines()
    dados = dados[1:]
    for dado in dados:
        linha = dado.decode('utf-8')
        linha = linha.strip()  # serve para tirar os \r\n etc
        usuario = linha.split(',')
        print(usuario)
        enviar_email(usuario[0], usuario[1])
        break

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}


def enviar_email(nome, email):
    cliente_ses.send_email(
        Source='confusaosk8@gmail.com',
        Destination={
            'BccAddresses': [],
            'CcAddresses': [],
            'ToAddresses': [
                email
            ]
        },
        Message={
            'Subject': {
                'Charset': 'utf-8',
                'Data': 'Mensagem do Projeto 2'
            },
            'Body': {
                'Html': {
                    'Charset': 'utf-8',
                    'Data': f'Olá, mensagem enviada via serverless sr/sra: {nome}. Boas vindas Serverless.'
                }
            }
        }
    )


envio_email({}, {})
