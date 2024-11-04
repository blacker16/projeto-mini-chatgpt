import os
from groq import Groq

# Defina a chave da API diretamente no codigo ou garanta que ela esteja configurada no ambiente certo
os.environ["GROQ_API_KEY"] = "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"

client = groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

#inicializa a lista de mensagens para manter o contexto da conversa
messages = []

while True:
    usuario = input("digite uma mensagem ou 'sair' para encerrar: ")

    if usuario.lower() == 'sair':
     print("conversa encerrada.")
     break

    #adiciona a mensagem do usuario a lista de mensagens
    messages.append({"role": "user", "content": usuario})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llams-3.1-70b-versatile",
    )

    resposta = chat_completion.choices[0].message.content
    print("resposta", resposta)

    #adiciona a resposta do assistente a lista de mensagens para manter o contexto da conversa
    messages.append({"role": "assistant", "content": resposta})    