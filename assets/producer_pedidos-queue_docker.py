import pika
import json

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('btg', 'itderiv')))
channel = connection.channel()

# Especificando a fila
fila_rabbitmq = "pedidos-queue"
channel.queue_declare(queue=fila_rabbitmq, durable=True)  # durable=True para garantir persistência da fila

# Carregando os pedidos do arquivo JSON
with open("pedidos_teste_mystore.json", "r") as arquivo:
    pedidos = json.load(arquivo)

# Loop para enviar cada pedido para a fila
for pedido in pedidos:
    mensagem = json.dumps(pedido)  # Serializar o pedido como JSON
    channel.basic_publish(
        exchange='',
        routing_key=fila_rabbitmq,
        body=mensagem,
        properties=pika.BasicProperties(delivery_mode=2)  # delivery_mode=2 para persistir as mensagens
    )

print(f"Enviados {len(pedidos)} pedidos para a fila '{fila_rabbitmq}'.")

# Fechando a conexão
connection.close()