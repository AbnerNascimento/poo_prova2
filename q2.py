class Motorista:
    def __init__(self, nome: str, idade: int, cpf: str):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    def __str__(self) -> str:
        return f"{self._nome} - {self._idade} anos - CPF: {self._cpf}"
    
class Veiculo:
    def __init__(self, numero: str, modelo: str):
        self._numero = numero
        self._modelo = modelo
        self._motorista = None

    def vincular_motorista(self, motorista: Motorista):
        self._motorista = motorista

    def __str__(self) -> str:
        return f"{self._numero} - {self._modelo}"


class Onibus(Veiculo):
    def __init__(self, numero: str, modelo: str, capacidade: int):
        super().__init__(numero, modelo)
        self._capacidade = capacidade

    def __str__(self) -> str:
        return f"{super().__str__()} (Capacidade: {self._capacidade})"




def controle_frota():
    frota = []
    motoristas = []

    while True:
        print("\n#___SISTEMA DE CONTROLE DE ÔNIBUS___#")
        print("1. cadastrar onibus\n2. cadastrar Motorista\n3. vincular motorista a onibus")
        print("4. Listar Motoristas\n5. Listar Ônibus\n0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero, modelo, capacidade = input("Número, Modelo, Capacidade: ").split()
            onibus = Onibus(numero, modelo, int(capacidade))
            frota.append(onibus)
            print(f"Ônibus {onibus} cadastrado com sucesso!")
        elif opcao == "2":
            nome, idade, cpf = input("Nome, Idade, CPF: ").split()
            motorista = Motorista(nome, int(idade), cpf)
            motoristas.append(motorista)
            print(f"Motorista {motorista} cadastrado com sucesso!")
        elif opcao == "3":
            print("\nLista de Ônibus disponíveis:")
            for i, onibus in enumerate(frota, 1):
                print(f"{i}. {onibus}")

            escolha_onibus = int(input("Escolha o número do ônibus: ")) - 1

            print("\nLista de Motoristas disponíveis:")
            for i, motorista in enumerate(motoristas, 1):
                print(f"{i}. {motorista}")

            escolha_motorista = int(input("Escolha o número do motorista: ")) - 1

            frota[escolha_onibus].vincular_motorista(motoristas[escolha_motorista])
            print(f"Motorista {motoristas[escolha_motorista]} vinculado ao ônibus {frota[escolha_onibus]}.")
        elif opcao == "4":
            print("\nLista de Motoristas:")
            for motorista in motoristas:
                print(motorista)
        elif opcao == "5":
            print("\nLista de Ônibus:")
            for onibus in frota:
                print(f"{onibus} (Motorista: {onibus._motorista})" if onibus._motorista else f"{onibus} (Sem motorista)")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    controle_frota()
