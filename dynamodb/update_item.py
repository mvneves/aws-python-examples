import boto3

# Inicializa o cliente do DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Nome da tabela
table_name = 'users'

# Define a chave primária e regra de atualização do item
# A tabela usa chave composta: é preciso informar a chave de partição e a de ordenação
key = {
    'username': {'S': 'joao.silva'},
    'last_name': {'S': 'Silva'}
}
update_expression = "SET age = :new_age"
expression_attribute_values = {
    ':new_age': {'N': '26'}
}

try:
    # Atualiza o item na tabela
    response = dynamodb_client.update_item(
        TableName=table_name,
        Key=key,
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )
    print(f"Item atualizado com sucesso na tabela {table_name}!")
except dynamodb_client.exceptions.ResourceNotFoundException:
    print(f"A tabela {table_name} não foi encontrada.")
except Exception as e:
    print(f"Erro ao atualizar item: {e}")
