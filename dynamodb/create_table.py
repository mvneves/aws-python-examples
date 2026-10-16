import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Definição da tabela
table_definition = {
    'TableName': table_name,
    'KeySchema': [
        {'AttributeName': 'username', 'KeyType': 'HASH'},  # Chave de partição
        {'AttributeName': 'last_name', 'KeyType': 'RANGE'}  # Chave de ordenação
    ],
    'AttributeDefinitions': [
        {'AttributeName': 'username', 'AttributeType': 'S'},
        {'AttributeName': 'last_name', 'AttributeType': 'S'}
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
}

try:
    # Cria a tabela
    response = dynamodb_client.create_table(**table_definition)

    # Aguarda a tabela ficar ativa antes de usá-la nos outros scripts
    dynamodb_client.get_waiter('table_exists').wait(TableName=table_name)
    print(f"Tabela {table_name} criada com sucesso!")
except dynamodb_client.exceptions.ResourceInUseException:
    print(f"A tabela {table_name} já existe.")
except Exception as e:
    print(f"Erro ao criar a tabela: {e}")
