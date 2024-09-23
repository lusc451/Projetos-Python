from flask import Flask, render_template, request

app = Flask(__name__)

# Definição das perguntas e alternativas do quiz
perguntas = [
    {
        "pergunta": "1. Qual é o nome do protagonista de One Piece?",
        "opcoes": ["Zoro", "Nami", "Luffy", "Sanji"],
        "resposta": "c"
    },
    {
        "pergunta": "2. Em 'Naruto', qual é a besta de cauda que está selada dentro de Naruto Uzumaki?",
        "opcoes": ["Ichibi", "Yonbi", "Kyuubi", "Nanabi"],
        "resposta": "c"
    },
    {
        "pergunta": "3. Qual é o nome do vilarejo de onde vem Gon Freecss em Hunter x Hunter?",
        "opcoes": ["Yorknew City", "Whale Island", "Heaven’s Arena", "Isla Baleia"],
        "resposta": "d"
    },
    {
        "pergunta": "4. Qual o nome do titã que Eren Yeager se transforma em Attack on Titan?",
        "opcoes": ["Titã Blindado", "Titã Colossal", "Titã Fêmea", "Titã de Ataque"],
        "resposta": "d"
    }
]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        pontuacao = 0
        respostas_usuario = request.form.to_dict()

        # Verifica cada resposta
        for idx, pergunta in enumerate(perguntas):
            resposta_correta = pergunta['resposta']
            resposta_selecionada = respostas_usuario.get(f'pergunta{idx}', '')
            
            if resposta_selecionada.lower() == resposta_correta:
                pontuacao += 1

        return render_template('resultado.html', pontuacao=pontuacao, total=len(perguntas))

    # Aqui passamos explicitamente a função enumerate para o Jinja2
    return render_template('quiz.html', perguntas=perguntas, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
