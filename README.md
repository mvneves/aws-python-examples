# AWS Python Examples

Exemplos de uso do Amazon S3 e do Amazon DynamoDB com o [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html),
o SDK da AWS para Python.

## Preparação

Instale o boto3 (de preferência num ambiente virtual):

    python3 -m venv .venv
    source .venv/bin/activate        # no Windows: .venv\Scripts\activate
    pip install boto3

### Credenciais do AWS Academy Learner Lab

As credenciais do Learner Lab são temporárias e mudam a cada sessão.

1. No Learner Lab, clique em **Start Lab** e depois em **AWS Details > AWS CLI: Show**.
2. Copie o bloco exibido para o arquivo `~/.aws/credentials` (no Windows, `%USERPROFILE%\.aws\credentials`). Ele tem
   as três linhas abaixo; sem o `aws_session_token`, os scripts falham com erro de credencial inválida:

   ```ini
   [default]
   aws_access_key_id=...
   aws_secret_access_key=...
   aws_session_token=...
   ```

3. Defina a região no arquivo `~/.aws/config`:

   ```ini
   [default]
   region = us-east-1
   ```

Repita o passo 2 sempre que iniciar uma nova sessão do laboratório.

## S3

Antes de executar, edite as variáveis no início de cada script (`bucket_name`, `key_name`, `file_path` etc.).

**Nomes de bucket são únicos no mundo inteiro:** os nomes dos exemplos (`meu-novo-bucket-unico`,
`nome-do-seu-bucket`) já existem ou vão colidir com os dos colegas. Use um nome próprio, por exemplo
`aula01-seunome-2027`, só com letras minúsculas, números e hífens.

Ordem sugerida:

1. `create_bucket.py` — cria o bucket (em `us-east-1`; em outra região é preciso informar
   `CreateBucketConfiguration={'LocationConstraint': '<região>'}`)
2. `list_buckets.py`
3. `put_object.py`, `put_object_json.py`, `upload_file.py`, `upload_multipart.py`, `metadata.py` — enviam objetos
4. `head_object.py`, `get_object.py`, `get_object_json.py`, `get_object_range.py`, `download_file.py` — leem objetos
5. `delete_object.py` — remove um objeto
6. `delete_bucket.py` — remove o bucket (ele precisa estar vazio)

## DynamoDB

Os scripts usam a tabela `users`, com chave composta: `username` (partição) e `last_name` (ordenação). Por isso,
toda operação sobre um item específico precisa informar **as duas** chaves.

Ordem sugerida:

1. `create_table.py` — cria a tabela e espera ela ficar ativa
2. `put_item.py`, `batch_write_item.py` — inserem itens
3. `get_item.py`, `batch_get_item.py`, `query_table.py`, `scan_table.py`, `limit_page.py` — leem itens
4. `update_item.py` — atualiza um item
5. `transact_write_items.py` — executa várias operações numa transação
6. `create_index.py` — cria um índice secundário global (GSI) por `email`
7. `delete_item.py` — remove um item

Ao terminar, apague a tabela para não consumir créditos:

    aws dynamodb delete-table --table-name users
