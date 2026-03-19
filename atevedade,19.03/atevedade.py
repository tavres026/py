def jogador(pontos, derrotas):
    pontos = pontos - 10 * derrotas

    if pontos < 0:
        return "Banido"
    if pontos >= 600:
        return "Diamante"
    if pontos >= 300:
        return "Ouro"
    if pontos >= 100:
        return "Prata"
    return "Bronze"


def saldo(saldo, saque):
    if saque > saldo:
        return "Saldo incopleto"

    taxa = 0
    if saque > 1000:
        taxa = saque * 0.02

    saldoo = saldo - saque - taxa
    return saldoo


def magia(fogo, agua):
    if fogo and agua:
        return "Vapor"
    if fogo:
        return "Fogo"
    if agua:
        return "Água"
    return "Sem magia"


def total(pontos, tempo):
    bonus = 0

    if tempo < 30:
        bonus = 50
    if tempo > 100:
        bonus = -20

    total = pontos + bonus

    if total > 200:
        return "Recorde"
    return total


def acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"

    usuario = (usuario == "admin")
    senha = (senha == "1234")

    if usuario and senha:
        return "Acesso liberado"
    if usuario:
        return "Senha errada"
    return "Usuário errado"



def foguete(combustivel, clima, sistema_ok):
    condicoes_ok = (
        combustivel >= 100 and
        clima == "bom" and
        sistema_ok
    )

    if condicoes_ok:
        return "Lançamento permitido"

    if combustivel < 100:
        return "Combustível incompleto"
    if clima != "bom":
        return "Clima ruim"
    return "Falha"