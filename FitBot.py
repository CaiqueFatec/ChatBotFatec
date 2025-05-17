import os
import telebot
from flask import Flask
from threading import Thread
import time

CHAVE_API = os.getenv("CHAVE_API")

bot = telebot.TeleBot(CHAVE_API)

usuarios = {}


@bot.message_handler(commands=["sac"])
def sac(message):
    bot.send_message(message.chat.id, "Caso queria falar com um dos nossos atendentes lique para 11940028922\nClique aqui para acessar nosso grupo de duvidas: https://t.me/+oXtY0G20XWQ2MmRh\n Para voltar ao inicio clique em /voltar")

@bot.message_handler(commands=["treinoCompleto"])
def treinoCompleto(message):
    texto = """
        Treino completo ABC para hipertrofia voltado para praticantes intermediários, com divisão clássica por grupamentos musculares. O foco é em sobrecarga progressiva e volume moderado a alto, ideal para promover crescimento muscular.

        🔹 Treino A – Peito, Ombro e Tríceps
        1. Supino reto com barra – 4x6-10
        2. Supino inclinado com halteres – 3x8-12
        3. Crucifixo com halteres (banco plano ou inclinado) –\n3x10-12
        4. Elevação lateral (ombros) – 3x12-15
        5. Desenvolvimento com halteres ou máquina – 3x8-12
        6. Tríceps testa (barra ou halteres) – 3x10-12
        7. Tríceps corda na polia – 3x12-15

        🔹 Treino B – Costas e Bíceps
        1. Barra fixa (livre ou assistida) – 4x6-10
        2. Remada curvada com barra – 3x8-10
        3. Puxada alta na polia (pegada aberta) – 3x10-12
        4. Remada unilateral com halteres – 3x10-12
        5. Rosca direta com barra – 3x8-12
        6. Rosca alternada com halteres – 3x10-12
        7. Rosca concentrada ou martelo – 3x12-15

        🔹 Treino C – Pernas e Abdômen
        1. Agachamento livre – 4x6-10
        2. Leg press – 3x10-12
        3. Cadeira extensora – 3x12-15
        4. Mesa flexora – 3x12-15
        5. Elevação de panturrilha sentado – 3x15-20
        6. Elevação de panturrilha em pé – 3x15-20
        7. Prancha abdominal – 3x30-60s
        8. Elevação de pernas – 3x15-20

        ✔️ Dicas gerais:
        Descanse de 60 a 90 segundos entre as séries.

        Treine 3 a 6 vezes por semana, com rotação dos treinos (ex: ABC, descanso, ABC...).

        Priorize boa execução e controle do movimento.

        Progrida cargas semanalmente quando possível.

        Faça já seu agendamento de treino, clique em /agendar
        \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)
    
@bot.message_handler(commands=["treinoA"])
def treinoA(message):
    texto = """
        🔹 Treino A – Peito, Ombro e Tríceps
        1. Supino reto com barra – 4x6-10
        2. Supino inclinado com halteres – 3x8-12
        3. Crucifixo com halteres (banco plano ou inclinado) –\n3x10-12
        4. Elevação lateral (ombros) – 3x12-15
        5. Desenvolvimento com halteres ou máquina – 3x8-12
        6. Tríceps testa (barra ou halteres) – 3x10-12
        7. Tríceps corda na polia – 3x12-15
        \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["treinoB"])
def treinoB(message):
    texto = """
        🔹 Treino B – Costas e Bíceps
        1. Barra fixa (livre ou assistida) – 4x6-10
        2. Remada curvada com barra – 3x8-10
        3. Puxada alta na polia (pegada aberta) – 3x10-12
        4. Remada unilateral com halteres – 3x10-12
        5. Rosca direta com barra – 3x8-12
        6. Rosca alternada com halteres – 3x10-12
        7. Rosca concentrada ou martelo – 3x12-15
        \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["treinoC"])
def treinoC(message):
    texto = """
        🔹 Treino C – Pernas e Abdômen
        1. Agachamento livre – 4x6-10
        2. Leg press – 3x10-12
        3. Cadeira extensora – 3x12-15
        4. Mesa flexora – 3x12-15
        5. Elevação de panturrilha sentado – 3x15-20
        6. Elevação de panturrilha em pé – 3x15-20
        7. Prancha abdominal – 3x30-60s
        8. Elevação de pernas – 3x15-20
        \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["treino"])
def treino(message):
    chat_id = message.chat.id
    plano = usuarios.get(chat_id, {}).get("plano")

    if not plano:
        bot.send_message(chat_id, "Você ainda não escolheu um plano. Acesse /planos para selecionar um.")
        return
    texto = """
            Clique em uma das opções a seguir para consultar seu treino
            /treinoCompleto Mostra o treino todo e as dicas
            /treinoA Treino A
            /treinoB Treino B
            /treinoC Treino C
            \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["planoBasico"])
def planoBasico(message):
    chat_id = message.chat.id
    usuarios.setdefault(chat_id, {})["plano"] = "Plano Básico"
    texto = """
        Obrigado por escolher o plano Básico, para consultar o seu treino clique em /treino \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["planoPadrao"])
def planoPadrao(message):
    chat_id = message.chat.id
    usuarios.setdefault(chat_id, {})["plano"] = "Plano Padrão"
    texto = """
        Obrigado por escolher o plano Padrão, para consultar o seu treino clique em /treino \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["planoPremium"])
def planoPremium(message):
    chat_id = message.chat.id
    usuarios.setdefault(chat_id, {})["plano"] = "Plano Premium"
    texto = """
        Obrigado por escolher o plano Premium, para consultar o seu treino clique em /treino \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["meuplano"])
def meu_plano(message):
    chat_id = message.chat.id
    plano = usuarios.get(chat_id, {}).get("plano")

    if plano:
        texto = f"Você está atualmente no {plano}. Para consultar seu treino, digite /treino, caso deseje alterar seu plano digite /alterarPlano"
    else:
        texto = "Você ainda não escolheu um plano. Por favor, veja nossas opções em /planos"
    bot.send_message(chat_id, texto)

@bot.message_handler(commands=["alterarPlano"])
def alterar_plano(message):
    chat_id = message.chat.id
    plano_atual = usuarios.get(chat_id, {}).get("plano")

    if plano_atual:
        texto = f"""
            Você está atualmente no {plano_atual}.
            Escolha um novo plano abaixo:

            🟢 /planoBasico  
            🔵 /planoPadrao  
            🟣 /planoPremium
            \nPara voltar ao inicio clique em /voltar
        """
    else:
        texto = "Você ainda não possui um plano ativo. Para ver os planos disponíveis, use /planos"

    bot.send_message(chat_id, texto)

@bot.message_handler(commands=["cadastro"])
def cadastro(message):
    chat_id = message.chat.id
    usuarios[chat_id] = {"estado": "aguardando_nome"}
    bot.send_message(chat_id, "📝 Vamos iniciar seu cadastro. Por favor, informe seu nome completo:")


@bot.message_handler(func=lambda msg: usuarios.get(msg.chat.id, {}).get("estado") == "aguardando_nome")
def receber_nome(message):
    chat_id = message.chat.id
    usuarios[chat_id]["nome"] = message.text
    usuarios[chat_id]["estado"] = "aguardando_telefone"
    bot.send_message(chat_id, "📞 Agora informe seu número de telefone (com DDD):")

@bot.message_handler(func=lambda msg: usuarios.get(msg.chat.id, {}).get("estado") == "aguardando_telefone")
def receber_telefone(message):
    chat_id = message.chat.id
    usuarios[chat_id]["telefone"] = message.text
    usuarios[chat_id]["estado"] = "aguardando_email"
    bot.send_message(chat_id, "📧 Por fim, informe seu email:")

@bot.message_handler(func=lambda msg: usuarios.get(msg.chat.id, {}).get("estado") == "aguardando_email")
def receber_email(message):
    chat_id = message.chat.id
    usuarios[chat_id]["email"] = message.text
    usuarios[chat_id]["estado"] = "cadastro_concluido"

    nome = usuarios[chat_id]["nome"]
    telefone = usuarios[chat_id]["telefone"]
    email = usuarios[chat_id]["email"]

    texto = f"""
        ✅ Cadastro concluído com sucesso!

        👤 Nome: {nome}
        📞 Telefone: {telefone}
        📧 Email: {email}

        Agora clique em /planos para conhecer nossos planos!
        \nPara voltar ao inicio clique em /voltar
    """
    bot.send_message(chat_id, texto)


@bot.message_handler(commands=["planos"])
def planos(message):
    chat_id = message.chat.id
    nome = usuarios.get(chat_id, {}).get("nome")

    if not nome:
        bot.send_message(chat_id, "Você precisa se cadastrar primeiro. Use o comando /cadastro.")
        return
    texto = f"""
        Olá {nome} seja muito bem vindo a nossa academia, escolha um de nossos planos!

        🟢 Plano Básico /escolhaBasico – Essencial para Começar

        🔵 Plano Padrão /escolhaPadrao – Equilíbrio e Evolução

        🟣 Plano Premium /escolhaPremium – Alta Performance e Conforto Total

        Para voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["escolhaBasico"])
def sobre(message):
    texto = """
            Plano Básico – Essencial para Começar
            Ideal para quem está iniciando na academia e quer manter a rotina com flexibilidade.

            Inclui:

            Acesso livre à musculação e aeróbicos

            Avaliação física gratuita na matrícula

            Acesso ao aplicativo com treinos básicos

            Horários: segunda a sexta, das 7h às 17h

            💰 Valor: R$ 79,90/mês
            🎓 Desconto especial para estudantes e professores: R$ 69,90/mês

            Clique aqui para confirmar sua escolha /planoBasico
            \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["escolhaPadrao"])
def sobre(message):
    texto = """
            Plano Padrão – Equilíbrio e Evolução
            Perfeito para quem busca variedade nas atividades e suporte completo.

            Inclui tudo do plano Básico, mais:

            Acesso a todas as aulas coletivas (yoga, ritmos, funcional, etc.)

            Horários estendidos: segunda a sexta, das 6h às 22h; sábados até 14h

            Personal trainer para orientação semanal

            Café fitness e wi-fi no espaço de convivência

            💰 Valor: R$ 119,90/mês
            🎓 Desconto Fatec: R$ 99,90/mês
            Clique aqui para confirmar sua escolha /planoPadrao
            \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["escolhaPremium"])
def sobre(message):
    texto = """
            Plano Premium – Alta Performance e Conforto Total
            Para quem leva a saúde a sério e quer um serviço completo e personalizado.

            Inclui tudo do plano Padrão, mais:

            Acompanhamento mensal individualizado com personal trainer

            Acesso livre todos os dias da semana, incluindo domingos e feriados

            Treinos personalizados com atualização quinzenal via app

            Convite para eventos exclusivos e workshops fitness

            1 massagem relaxante por mês incluída

            💰 Valor: R$ 169,90/mês
            🎓 Desconto Fatec: R$ 139,90/mês
            Clique aqui para confirmar sua escolha /planoPremium
            \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["sobre"])
def sobre(message):
    texto = """
        Bem-vindo à FatecFit – Transforme seu Corpo, Eleve sua Mente!

        A FatecFit é mais do que uma academia: é um espaço moderno, acolhedor e motivador para quem busca saúde, bem-estar e resultados reais. Localizada próxima à Fatec, nossa estrutura é pensada tanto para iniciantes quanto para atletas experientes, com equipamentos de última geração, ambiente climatizado e acompanhamento profissional qualificado.

        O que você encontra na FatecFit:

        💪 Musculação completa com aparelhos de ponta

        🧘 Aulas coletivas: funcional, yoga, pilates, ritmos e mais

        🏃 Treinamento cardiovascular com esteiras, bikes e    elípticos

        📲 Avaliação física gratuita na matrícula

        🧑‍🏫 Personal trainers e profissionais de educação física sempre por perto

        ☕ Espaço de convivência com wi-fi e café fitness

        Vantagens exclusivas:

        Planos acessíveis para estudantes e professores

        Aplicativo com treinos personalizados e controle de progresso

        Horários flexíveis, inclusive aos finais de semana

        Venha conhecer a FatecFit e experimente uma aula grátis! Aqui, seu objetivo é levado a sério, e o seu bem-estar é prioridade. Cadastre-se e comece hoje sua jornada de transformação! /cadastro
        \nPara voltar ao inicio clique em /voltar
            """
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=["agendar"])
def agendar_treino(message):
    chat_id = message.chat.id

    if usuarios.get(chat_id, {}).get("plano") is None:
        bot.send_message(chat_id, "Você precisa escolher um plano antes de agendar um treino. Acesse /planos.")
        return

    usuarios[chat_id]["estado"] = "aguardando_agendamento"
    bot.send_message(chat_id, "Digite o dia e horário que deseja agendar seu treino (ex: Segunda às 18h):")

@bot.message_handler(func=lambda msg: usuarios.get(msg.chat.id, {}).get("estado") == "aguardando_agendamento")
def receber_agendamento(message):
    chat_id = message.chat.id
    horario = message.text

    usuarios[chat_id]["agendamento"] = horario
    usuarios[chat_id]["estado"] = None  # limpa o estado

    bot.send_message(chat_id, f"✅ Treino agendado para: {horario}.\nSe quiser reagendar, use /agendar novamente.\nPara voltar ao inicio clique em /voltar")


@bot.message_handler(commands=["meuAgendamento"])
def meu_agendamento(message):
    chat_id = message.chat.id
    agendamento = usuarios.get(chat_id, {}).get("agendamento")

    if agendamento:
        bot.send_message(chat_id, f"📅 Seu treino está agendado para: {agendamento}")
    else:
        bot.send_message(chat_id, "Você ainda não tem um treino agendado. Use /agendar para marcar.")

@bot.message_handler(func=lambda msg: msg.text.lower() in ["voltar", "menu", "início"])
def voltar_ao_inicio(message):
    texto = """
        Escolha uma das opções para continuar (clique no item):
         /sobre Saiba mais sobre a nossa academia.
         /cadastro Faça já o seu cadastro.
         /treino Consulte seu treino.
         /meuplano Consulte seu plano atual caso inscrito.
         /meuAgendamento Consulte seu agendamento de treino.
         /sac Fale com um des nossos atendentes.
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções
            """
    bot.send_message(message.chat.id, texto)


def verificar(mensagem):
    chat_id = mensagem.chat.id
    return not (chat_id in usuarios and usuarios[chat_id].get("estado") == "aguardando_nome")

@bot.message_handler(func=verificar)
def responder(mensagem):
    print(mensagem)
    texto = """
        Escolha uma das opções para continuar (clique no item):
         /sobre Saiba mais sobre a nossa academia.
         /cadastro Faça já o seu cadastro.
         /treino Consulte seu treino.
         /meuplano Consulte seu plano atual caso inscrito.
         /meuAgendamento Consulte seu agendamento de treino.
         /sac Fale com um des nossos atendentes.
        Responder qualquer outra coisa não vai funcionar, clique em uma das opções
            """
    bot.reply_to(mensagem, texto)

app = Flask('')

@app.route('/')
def home():
    return "Bot está rodando"

def manter_online():
    app.run(host='0.0.0.0', port=8080)

def iniciar_bot():
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(f"[ERRO] Bot caiu: {e}")
            time.sleep(5)

Thread(target=manter_online).start()
iniciar_bot()