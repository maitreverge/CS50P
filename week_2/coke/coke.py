def main():
    coke_price = 50
    total_coins = 0
    accepted_coins = (25, 10, 5)

    while total_coins < coke_price:
        print(f"Amount Due: {coke_price - total_coins}")
        current_coin = int(input("Insert Coin :"))

        if current_coin in accepted_coins:
            total_coins += current_coin

    print(f"Change Owed: {total_coins - coke_price}")


if __name__ == "__main__":
    main()
