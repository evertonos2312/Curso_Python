velocidade = input('Qual é a velocidade atual do carro? ')

if velocidade.isdigit():
    velocidade = float(velocidade)

    if velocidade > 80:
        print('MULTADO! Você excedeu o limite pertimido que é de 80km/h')
        multa = (velocidade - 80) * 7
        print(f'Você deve pagar uma multa de R$ {multa:.2f}')
    print('Tenha um bom dia! Dirija com segurança!')
