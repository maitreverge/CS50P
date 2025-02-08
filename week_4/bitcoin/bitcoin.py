import requests
import pprint
import json
import sys


def exit(message: str):
    print(message)
    sys.exit(1)


def get_btc(nb_btc: float) -> float:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        json_data = json.loads(r.text)
    except:
        print("Failed getting BTC Price, aborting...")
        sys.exit(1)

    # print(json.dumps(json_data))
    # pprint.pprint(json_data)
    rate = json_data["bpi"]["USD"]["rate"].replace(",", "")
    return float(rate) * nb_btc


def main():
    try:
        assert len(sys.argv) == 2
        nb_btc = float(sys.argv[1])
    except AssertionError:
        exit(
            "Programs required one CLI <float> argument\nExample : python3 bitcoin.py 1.5"
        )
    except:
        exit("CLI argument is not a number")

    value_btc = get_btc(nb_btc)
    print(f"${value_btc:,.04f}")


if __name__ == "__main__":
    main()
