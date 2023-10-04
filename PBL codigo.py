'''/**************************** 
 Autor: Letícia Gonçalves Souza
 Componente Curricular: MI algoritmos  
 Concluido em:25/09/2022 
 Declaro que este código foi elaborado por mim de forma individual e não contém nenhum  
 trecho de código de colega ou de outro autor, tais como provindos de livros e apostilas,
 e páginas ou documentos eletrônicos da internet. Qualquer trecho de código de outra 
 autoria que não a minha está destacado com uma citação do autor e a fonte do código, e estou  
 ciente que estes trechos não serão considerados para fins de avaliação. 
 /*****************************'''


# FUNÇÃO PARA VERIFICAÇÃO DAS ENTRADAS NUMERICAS 
def isNunber(comp,larg,estado,arv,opção):
    try:
        float(comp,larg,estado,arv,opção)
    except ValueError:
        return False
    return True

# VARIAVEIS ACUMULADORAS DOS ESTADOS
alagoas =  bahia =  ceara =  maranhao =  paraiba =  pernabuco =  piaui =  riogrande =  sergipe = 0

# Variavel das areas
arealagoas = arebahia = areceara = aremaranhao = areparaiba = arepernabuco = arepiaui = areriogrande = aresergipe = 0

# VARIAVEIS ACUMULADORAS DAS ARVORES
bambu = caju = coque = dende = ipe = mangueira = 0

# AREA DAS ARVORES
arebambu = arecaju = arecoque = aredende = areipe = aremangueira = 0

#VARIAVEIS PARA OS NOMES
estnome = arvnome = estmenosref = arvmais = arvmenos = ''

# VARIAVEIS DA RELACIONADAS A MAIOR AREA
maiorare = maiorest = 0
maiorcod = ''
maiorcid = maiorarv = 0

# TOTAL DO NORDESTE REFLORESTADO
aretotnordeste = 0

print('Bem vindo ao banco de dados da Reflorestar é viver.')
opção = 0
# MENU PRINCIPAL
while int(opção) != 3:
    print('=-=' * 10)
    print('''    [ 1 ]Realizar cadastro da área 
    [ 2 ]Emitir relatorio de reflorestamento 
    [ 3 ]Fechar programa''')
    print('=-=' * 10)
    print('!ATENÇÃO! Se você ainda não cadastrou nenhuma area digite 1 antes de emitir seu relatorio')
    print('=-=' * 10)
    opção = input('Qual a sua opção?')
    #VERIFICAÇÃO PARA O INPUT DA VARIAVEL OPÇÃO
    if type(opção) != int:
        while opção.isdigit() == False:
            print('Valor inválido')
            opção = input('Qual a sua opção?')
    while int(opção)<=0:
        print('Valor inválido')
        opção = input('Qual a sua opção?')  
    while int(opção)>3:
            print('Valor inválido')
            opção = input('Qual a sua opção?')    
    # CADASTRO DAS AREAS
    if int(opção) == 1:
        cod = str(input('Insira o código da área: '))
        print('=-=' * 10)
        # ESTADOS
        print('Qual estado corresponde a área?')
        print('''        [ 1 ]Alagoas [ 2 ]Bahia [ 3 ]Ceará 
        [ 4 ]Maranhão [ 5 ]Paraíba [ 6 ]Pernambuco 
        [ 7 ]Piauí [ 8 ]Rio Grande do Norte [ 9 ]Sergipe''')
        estado = input('Qual a sua opção?')
        #VERIFICAÇÃO DO INPUT DA VARIAVEL ESTADO
        if type(estado) != int:
            while estado.isdigit() == False:
                print('Valor inválido')
                estado = input('Qual a sua opção?') 
        while int(estado)>9:
            print('Valor inválido')
            estado = input('Qual a sua opção?')
        while int(estado)<=0:
            print('Valor inválido')          
            estado = input('Qual a sua opção?')
        print('=-=' * 10)
        
        cidade = str(input('Insira a cidade correspondente a área: '))
        print('=-=' * 10)
        
        comp = input('Insira o comprimento da área em metros: ')
        # VERIFICAÇÃO DO INPUT DA VARIAVEL REFERENTE A COMPRIMENTO(COMP)
        if type(comp) != int:
            while comp.isdigit() == False:
                print('Valor inválido')
                comp = input('Insira o comprimento da área em metros: ')
        while int(comp)<=0:
            print('Valor inválido')
            comp = input('Insira o comprimento da área em metros: ')
        
        larg = input('Insira a largura da área em metros: ')
        # VERIFICAÇÃO DO INPUT DA VARIAVEL REFERENTE A LARGURA(LARG)
        if type(larg) != int:
            while larg.isdigit() == False:
                print('Valor inválido')
                larg = input('Insira a largura da área em metros: ')       
        while int(larg)<=0:
            print('Valor inválido')
            larg = input('Insira a largura da área em metros: ')
       
       # CALCULO DE AREA
        are = int(comp) * int(larg)
        
        # CONDIÇÕES PARA GUARDAR AS INFORMAÇÕES DOS ESTADOS
        if int(estado) == 1:
            alagoas += 1
            arealagoas += are
            estnome = 'Alagoas'

        elif int(estado) == 2:
            bahia += 1
            arebahia += are
            estnome = 'Bahia'

        elif int(estado) == 3:
            ceara += 1
            areceara += are
            estnome = 'Ceará'

        elif int(estado) == 4:
            maranhao += 1
            aremaranhao += are
            estnome = 'Maranhão'

        elif int(estado) == 5:
            paraiba += 1
            areparaiba += are
            estnome = 'Paraíba'

        elif int(estado) == 6:
            pernabuco += 1
            arepernabuco += are
            estnome = 'Pernambuco'

        elif int(estado) == 7:
            piaui += 1
            arepiaui += are
            estnome = 'Piauí'

        elif int(estado) == 8:
            riogrande += 1
            areriogrande += are
            estnome = 'Rio Grande do Norte'

        elif int(estado) == 9:
            sergipe += 1
            aresergipe += are
            estnome = 'Sergipe'

        # CALCULO DA AREA TOTAL REFLORESTADA DO NORDESTE
        aretotnordeste = arealagoas + arebahia + areceara + aremaranhao + areparaiba + arepernabuco + arepiaui + areriogrande + aresergipe

        print('=-=' * 10)
        # ARVORES
        print('Qual árvore foi utilizada?')
        print('[ 1 ]Bambu gigante [ 2 ]Cajueiro [ 3 ]Coqueiro \n  [ 4 ]Dendê [ 5 ]Ipê [ 6 ]Mangueira')

        arv = input('Qual sua opção?')
        # VERIFICAÇÃO DP INPUT DA VARIAVEL REFERENTE A ARVORES(ARV)
        if type(arv) != int:
            while arv.isdigit() == False:
                print('Valor inválido')
                arv = input('Qual a sua opção?')
        while int(arv)>6:
            print('Valor inválido')
            arv= input('Qual a sua opção?')
        while int(arv)<=0:
            print('Valor inválido')
            arv= input('Qual a sua opção?')
       
       # CONDIÇÕES PARA GUARDAR AS INFOS DAS ARVORES
        if int(arv) == 1:
            bambu += 1
            arebambu += are
            arvnome = 'Bambu Gigante'

        elif int(arv) == 2:
            caju += 1
            arecaju += are
            arvnome = 'Cajueiro'

        elif int(arv) == 3:
            coque += 1
            arecoque += are
            arvnome = 'Coqueiro'

        elif int(arv) == 4:
            dende += 1
            aredende += are
            arvnome = 'Dendê'

        elif int(arv) == 5:
            ipe += 1
            areipe += are
            arvnome = 'Ipê'

        elif int(arv) == 6:
            mangueira += 1
            aremangueira += are
            arvnome = 'Mangueira'

        # INFO DA MAIOR AREA
        if maiorare < are:
            maiorare = are
            maiorest = estnome
            maiorcod = cod
            maiorcid = cidade
            maiorarv = arvnome

    # RELATORIO DE REFLORESTAMENTO
    if int(opção) == 2 and aretotnordeste != 0:
        print('=-=' * 10)
        print('RELÁTORIO DE REFLORESTAMENTO: ')
        print('A area total reflorestada por estado: \n Alagoas: {} m² \n Bahia: {} m² \n Ceará: {} m² \n Maranhão: {} m² \n Paraíba: {} m² \n Pernanbuco: {} m² \n Piauí: {} m² \n Rio Grande do Norte: {} m² \n Sergipe: {} m²'.format(
            arealagoas, arebahia, areceara, aremaranhao, areparaiba, arepernabuco, arepiaui, areriogrande, aresergipe))
        print('=-=' * 10)
        print('A area total reflorestada da região nordeste: {} m²'.format(aretotnordeste))
        print('=-=' * 10)
        print('Area total reflorestada por cada tipo de árvore: \n Bambu Gigante: {} m² \n Cajueiro: {} m² \n Coqueiro: {} m² \n Dendê: {} m² \n Ipê: {} m² \n Mangueira: {} m² '.format(
            arebambu, arecaju, arecoque, aredende, areipe, aremangueira))
       
        print('=-=' * 10)
       # COMPARAÇÃO DAS ARVORES MAIS USADAS
        print('A árvore mais utilizada nos reflorestamentos:')
        if bambu > caju and bambu > coque and bambu > dende and bambu > ipe and bambu > mangueira:
            print('Bambu Gigante: {} vezes'.format(bambu))

        elif caju > bambu and caju > coque and caju > dende and caju > ipe and caju > mangueira:
            print('Cajueiro: {} vezes'.format(caju))

        elif coque > bambu and coque > caju and coque > dende and coque > ipe and coque > mangueira:
            print('Coqueiro:{} vezes'.format(coque))

        elif dende > bambu and dende > caju and dende > coque and dende > ipe and dende > mangueira:
            print('Dendê: {} vezes'.format(dende))

        elif ipe > bambu and ipe > caju and ipe > coque and ipe > dende and ipe > mangueira:
            print('Ipê: {} vezes'.format(ipe))

        elif mangueira > bambu and mangueira > caju and mangueira > coque and mangueira > dende and mangueira > ipe:
            print('Mangueira: {}'.format(mangueira))
        
        print('=-=' * 10)
        
        #COMPARAÇÃO DA ARVORE MENOS USADA
        print('A árvore menos utilizada:')
        if bambu <= caju and bambu <= coque and bambu <= dende and bambu <= ipe and bambu <= mangueira:
           print('Bambu Gigante: {} vezes'.format(bambu))

        if caju <= bambu and caju <= coque and caju <= dende and caju <= ipe and caju <= mangueira:
            print('Cajueiro: {} vezes'.format(caju))

        if coque <= bambu and coque <= caju and coque <= dende and coque <= ipe and coque <= mangueira:
            print('Coqueiro: {} vezes'.format(coque))

        if dende <= bambu and dende <= caju and dende <= coque and dende <= ipe and dende <= mangueira:
            print('Dendê: {} vezes'.format(dende))

        if ipe <= bambu and ipe <= caju and ipe <= coque and ipe <= dende and ipe <= mangueira:
            print('Ipê: {} vezes'.format(ipe))

        if mangueira <= bambu and mangueira <= caju and mangueira <= coque and mangueira <= dende and mangueira <= ipe:
            print('Mangueira: {}'.format(mangueira))
       
        print('=-=' * 10)
        print('Informações da maior extensão reflorestada: \n Código: {} \n Estado: {} \n Cidade: {} \n Área: {} m² \n Árvore: {}'. format(
            maiorcod, maiorest, maiorcid, maiorare, maiorarv))
        print('=-=' * 10)
        print('Quantidade de áreas reflorestadas por estado: \n Alagoas: {} \n Bahia: {} \n Ceará: {} \n Maranhão: {} \n Paraíba: {} \n Pernambuco: {} \n Piauí {} \n Rio Grande do Norte: {} \n Sergipe: {}'.format(
            alagoas, bahia, ceara, maranhao, paraiba, pernabuco, piaui, riogrande, sergipe))
        print('=-=' * 10)
       
        #COMPARAÇÃO DO ESTADO MENOS REFLORESTADO       
        print('O estado menos reflorestado em relação a dimensão: ')
        if (arealagoas<=arebahia and arealagoas<=areceara and arealagoas<=aremaranhao and arealagoas<=areparaiba and arealagoas<=arepernabuco and arealagoas<=arepiaui and arealagoas<=areriogrande and arealagoas<=sergipe):
            print('Alagoas: {} m²'.format(arealagoas))
        
        if (arebahia<=arealagoas and arebahia<=areceara and arebahia<=aremaranhao and arebahia<=areparaiba and arebahia<=arepernabuco and arebahia<=arepiaui and arebahia<=areriogrande and arebahia<=aresergipe):
            print('Bahia: {} m²'.format(arebahia))

        if (areceara<=alagoas and areceara<=arebahia and areceara<=aremaranhao and areceara<=areparaiba and areceara<=arepernabuco and areceara<=arepiaui and areceara<=areriogrande and areceara<=aresergipe):
            print('Ceará: {} m²'.format(areceara))
        
        if (aremaranhao<=arealagoas and aremaranhao<=arebahia and aremaranhao<=areceara and aremaranhao<=areparaiba and aremaranhao<=arepernabuco and aremaranhao<=arepiaui and aremaranhao<=areriogrande and aremaranhao<=aresergipe):
            print('Maranhão: {} m²'.format(aremaranhao))

        if (areparaiba<=arealagoas and areparaiba<=arebahia and areparaiba<=areceara and areparaiba<=aremaranhao and areparaiba<=arepernabuco and areparaiba<=arepiaui and areparaiba<=areriogrande and areparaiba<=aresergipe):
            print('Paraíba: {} m²'.format(areparaiba))
        
        if (arepernabuco<=arealagoas and arepernabuco<=arebahia and arepernabuco<=areceara and arepernabuco<=aremaranhao and arepernabuco<=areparaiba and arepernabuco<=arepiaui and arepernabuco<=areriogrande and arepernabuco<=aresergipe):   
            print('Pernambuco: {} m²'.format(arepernabuco))
        
        if (arepiaui<=arealagoas and arepiaui<=arebahia and arepiaui<=areceara and arepiaui<=aremaranhao and arepiaui<=areparaiba and arepiaui<=arepernabuco and arepiaui<=areriogrande and arepiaui<=aresergipe):
            print('Piauí: {} m²'.format(arepiaui))
        
        if (areriogrande<=arealagoas and areriogrande<=arebahia and areriogrande<=areceara and areriogrande<=aremaranhao and areriogrande<=areparaiba and areriogrande<=arepernabuco and areriogrande<=arepiaui and areriogrande<=aresergipe):
            print('Rio Grande do Norte: {} m²'.format(areriogrande))
        
        if (aresergipe<=arealagoas and aresergipe<=arebahia and aresergipe<=areceara and aresergipe<=aremaranhao and aresergipe<=areparaiba and aresergipe<=arepernabuco and aresergipe<=arepiaui and aresergipe<=areriogrande):
            print('Sergipe: {} m²'.format(aresergipe))
    
    # CONDIÇÃO PARA MOSTRAR MENSAGEM SE NENHUMA AREA CADASTRADA TIVER SIDO CADASTRADA
    if int(opção) == 2 and aretotnordeste == 0: 
        print('=-=' * 10)
        print('=-=' * 10)
        print('Você ainda não possui áreas cadastradas')
        print('=-=' * 10)
    # ENCERRADOR DO PROGRAMA
    if int(opção) == 3:
        print('Programa encerrado, volte sempre!')
        