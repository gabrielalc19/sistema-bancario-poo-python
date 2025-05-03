class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def saldo_atual(self):
        return self.saldo


def main():
    contas = []

    print("=== Sistema Bancário ===")
    print("Digite as contas no formato: Nome, SaldoInicial")
    print("Digite 'FIM' para encerrar e listar as contas cadastradas.\n")

    while True:
        entrada = input()
        if entrada.strip().upper() == "FIM":
            break
        try:
            nome, saldo = entrada.split(",")
            nome = nome.strip()
            saldo = float(saldo.strip())
            conta = ContaBancaria(nome, saldo)
            contas.append(conta)
        except ValueError:
            print("Entrada inválida. Use o formato: Nome, SaldoInicial")

    print("\nContas cadastradas:")
    saida = ", ".join([f"{conta.titular}: R$ {int(conta.saldo_atual())}" for conta in contas])
    print(saida)


if __name__ == "__main__":
    main()
