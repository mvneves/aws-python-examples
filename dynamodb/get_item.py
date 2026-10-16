import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

try:
    # Lê o item da tabela (a chave composta exige username e last_name)
    response = dynamodb_client.get_item(
        TableName=table_name,
        Key={'username': {'S': 'joao.silva'}, 'last_name': {'S': 'Silva'}}
    )
    
    # Verifica se o item foi encontrado
    if 'Item' in response:
        item = response['Item']
        print(f"Item encontrado: {item}")
    else:
        print(f"Item não foi encontrado na tabela {table_name}.")
except dynamodb_client.exceptions.ResourceNotFoundException:
    print(f"A tabela {table_name} não foi encontrada.")
except Exception as e:
    print(f"Erro ao ler item: {e}")

