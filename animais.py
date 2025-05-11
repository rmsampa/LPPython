perguntas = [ ['Seu animal gosta de bananas?', 'macaco'] ]

while True:
  print('Pense em um animal...')

  acertou = False
  for pergunta in perguntas:

    resposta = input(f'{pergunta[0]} (s/n) ')
    if resposta.lower() == 's':
        print(f'Você pensou em {pergunta[1]}!')
        acertou = True
        break
  
  if not acertou:
    animal = input('Desisto! Em qual animal você estava pensando? ')
    novapergunta = input('Qual pergunta poderia me ajudar a adivinhar o animal? ')
    
    perguntas.append([ novapergunta, animal ])

    resposta = input('Você quer continuar? (s/n): ')
    if resposta.lower() != 's':
      print('ok! foi bom brincar com você!')
      break

