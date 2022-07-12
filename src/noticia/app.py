import json
from noticia import Noticia


def lambda_handler(event, context):
    print(event)

    noticia = Noticia()

    if 'path' in event:
        if event['path'] == '/consultar/noticia':
            body = {
                "content": noticia.consultar_noticia()
            }

        elif event['path'] == '/listar/noticias':
            body = noticia.listar_noticias()

        elif event['path'] == '/upload/noticia':
            event_body = json.loads(event['body'])
            noticia.content = event_body['content']
            noticia.upload_noticia()

            body = {
                "content": noticia.id
            }
    else:
        noticia.id = event['id']
        noticia.content = event['detail']['content']
        noticia.store_noticia()

        body = {
            "content": "eventbrige event"
        }

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
