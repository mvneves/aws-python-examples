import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Lista de usuários a serem buscados: (username, last_name), pois a tabela usa chave composta
users_to_get = [
    ('joao.silva', 'Silva'),
    ('maria.pereira', 'Pereira'),
    ('ana.santos', 'Santos'),
    ('pedro.souza', 'Souza')
]

# Converta a lista de usuários em uma lista de dicionários de chaves
keys_to_get = [
    {'username': {'S': username}, 'last_name': {'S': last_name}}
    for username, last_name in users_to_get
]

response = dynamodb_client.batch_get_item(
    RequestItems={
        table_name: {
            'Keys': keys_to_get
        }
    }
)

items = response['Responses'][table_name]
for item in items:
    print(item)

