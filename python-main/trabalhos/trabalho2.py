def calcula_media_enem():
    
    linguagens = 0
    while linguagens < 1 or linguagens > 1000:
        linguagens = float(input("Entre com a nota em Linguagens (0-1000): "))

    ciencias_humanas = 0
    while ciencias_humanas < 1 or ciencias_humanas > 1000:
        ciencias_humanas = float(input("Entre com a nota em Ciências Humanas (0-1000): "))

    ciencias_natureza = 0
    while ciencias_natureza < 1 or ciencias_natureza > 1000:
        ciencias_natureza = float(input("Entre com a nota em Ciências da Natureza (0-1000): "))

    matematica = 0
    while matematica < 1 or matematica > 1000:
        matematica = float(input("Entre com a nota em Matemática (0-1000): "))

    redacao = 0
    while redacao < 1 or redacao > 1000:
        redacao = float(input("Entre com a nota em Redação (0-1000): "))

    
    if 0 <= linguagens <= 1000 and 0 <= ciencias_humanas <= 1000 and 0 <= ciencias_natureza <= 1000 and 0 <= matematica <= 1000 and 0 < redacao <= 1000:
        media = (linguagens + ciencias_humanas + ciencias_natureza + matematica + redacao) / 5
        print("Sua média final é:", media)

        
        if media >= 450 and redacao > 0:
            print("Parabéns! Você está aprovado no Prouni e no Fies.")
        else:
            print("Infelizmente, você não está aprovado no Prouni e no Fies.")


calcula_media_enem()
