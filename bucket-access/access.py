import boto3

# Substitua 'YOUR_ACCESS_KEY_ID' e 'YOUR_SECRET_ACCESS_KEY' com suas credenciais da AWS
ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'

# Substitua 'YOUR_BUCKET_NAME' com o nome do seu bucket
BUCKET_NAME = 'YOUR_BUCKET_NAME'

def list_objects():
    # Inicialize o cliente S3 com suas credenciais
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    
    # Liste todos os objetos no bucket
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print("O bucket está vazio.")
    except Exception as e:
        print(f"Erro ao listar objetos no bucket: {e}")

if __name__ == "__main__":
    list_objects()

