#On your Windows terminal, type: pip install requests
#That's the only library required.
import requests 
 


def main():
    print('#######  Consulta CEP  #######')
    
    while True:
        cep_input = input('Digite o CEP para consulta: ')
        if len(cep_input) != 8:
            print('CEP inválido. Digite no formato 00000000 com 8 dígitos.')
        else:
            break 

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input)) 
    adress_data = request.json()


    
    if 'erro' not in adress_data:
            print('>>> CEP Encontrado <<<')
            print('Cep: {}'.format(adress_data['cep']))
            print('Logradouro: {}'.format(adress_data['logradouro']))
            print('Complemento: {}'.format(adress_data['complemento']))
            print('Bairro: {}'.format(adress_data['bairro']))
            print('Cidade: {}'.format(adress_data['localidade']))
            print('Estado: {}'.format(adress_data['uf']))
            print('ddd: {}\n'.format(adress_data['ddd']))

    else:
            print('CEP inválido.')


    option = int(input("\nDeseja fazer mais uma busca? \n1. Sim\n2. Sair\n"))
    if option == 1:
        print("________________\n")
        main()
        
    else:
        print("Saindo...")

     
    

if __name__ == '__main__':
    main()
