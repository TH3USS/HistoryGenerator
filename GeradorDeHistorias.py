import openai

# Defina sua chave de API do OpenAI
openai.api_key = "SUA_API_KEY_AQUI"

# Função para gerar uma história com base na escolha do usuário
def gerar_historia(escolha_usuario):
    prompt = f"Crie uma história interessante baseada na seguinte escolha: {escolha_usuario}. A história deve ser envolvente e ter pelo menos três parágrafos."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um escritor criativo que cria histórias envolventes."},
                {"role": "user", "content": prompt}
            ]
        )

        historia = response['choices'][0]['message']['content']
        return historia

    except Exception as e:
        return f"Erro ao gerar a história: {e}"

# Interface simples no terminal para o usuário
if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Histórias Interativas!")
    escolha = input("Digite um tema ou escolha para a sua história: ")

    historia = gerar_historia(escolha)
    print("\nAqui está a sua história gerada:\n")
    print(historia)
