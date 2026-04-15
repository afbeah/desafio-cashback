def calcular_cashback(valor_compra, percentual_desconto, tipo_cliente):
    valor_final = valor_compra * (1 - percentual_desconto / 100)

    cashback_base = valor_final * 0.05
    cashback_total = cashback_base

    if tipo_cliente.lower() == "vip":
        bonus_vip = cashback_base * 0.10
        cashback_total += bonus_vip

    if  valor_final > 500:
        cashback_total *= 2

    return cashback_total

if __name__ == "__main__":
    resultado = calcular_cashback(600, 20, "vip")
    print(f"Cashback VIP: R$ {resultado:.2f}")