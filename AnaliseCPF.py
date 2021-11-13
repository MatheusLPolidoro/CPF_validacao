def digito_cpf(lista, numero_inicial, numero_final):
    soma_cpf = sum([(numero_inicial - index) * int(value) if index <
                   numero_final else 0 for index, value in enumerate(lista)])
    return '0' if soma_cpf % 11 < 2 else str(11 - soma_cpf % 11)


class NumeroCPF:
    def __init__(self, numero_cpf):
        cpf = [value for value in list(numero_cpf) if ord(
            value) >= 48 and ord(value) <= 57]
        self.numero_cpf = cpf if len(cpf) != 0 else []
        self.numero_valido = True
        self.resultado_calculo = None
        if len(self.numero_cpf) == 11 and ''.join(cpf).replace(numero_cpf[0], '') != '':
            self.digitos_verificadores = list(numero_cpf[len(numero_cpf)-2:])
        else:
            self.numero_valido = False

    def gerar_digitos_verificadores(self):
        if self.numero_valido != False:
            primeiro_digito = digito_cpf(self.numero_cpf, 10, 9) # 1º argumento: Lista, 2º argumento: qual digito gerar(10), 3º quantidade de números para percorrer
            segundo_digito = digito_cpf(self.numero_cpf, 11, 10) # 1º argumento: Lista, 2º argumento: qual digito gerar(11), 3º quantidade de números para percorrer
            self.resultado_calculo = [primeiro_digito, segundo_digito]
        else:
            self.resultado_calculo = None
        return self.resultado_calculo

    def confirmar_digitos_verificadores(self):
        if self.numero_valido != False:
            if self.digitos_verificadores != self.resultado_calculo:
                self.numero_valido = False
        return self.numero_valido

    def mostrar_resultado(self):
        cpf = ''.join(self.numero_cpf)
        self.cpf_formatado = '{}.{}.{}-{}'.format(
            cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        print("CPF: %s Válido!" % ''.join(self.cpf_formatado)) if self.numero_valido == True else print(
            "CPF: %s Inválido!" % ''.join(self.cpf_formatado))

    def consultar_regiao(self):
        if (len(self.numero_cpf) == 11):
            self.estados = {
                '1': 'DF, GO, MS, MT e TO',
                '2': 'AC, AM, AP, PA, RO e RR',
                '3': 'CE, MA e PI',
                '4': 'AL, PB, PE, RN',
                '5': 'BA e SE',
                '6': 'MG',
                '7': 'ES e RJ',
                '8': 'SP',
                '9': 'PR e SC',
                '0': 'RS'
            }
            return [self.numero_cpf[8], self.estados]
        else:
            return ['inicial', None]
