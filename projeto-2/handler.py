import json
import boto3

sessao = boto3.Session(profile_name='automacao-curso', region_name='us-east-1')
cliente_s3 = sessao.client('s3')


def envio_email(event, context):
    resultado = cliente_s3.get_object(
        Bucket='send-email-ses-projeto2',
        Key='usuarios.csv'
    )

    dados = resultado['Body'].readlines()
    for dado in dados:
        linha = dado.decode('utf-8')
        linha = linha.strip() # serve para tirar os \r\n etc
        usuario = linha.split(',')
        print(usuario)

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}

envio_email({}, {})