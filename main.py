import json


def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(
    amount: float,
    base: str, to: str,
    rates: dict[str, dict]
     ) -> float:
    base: str = base.lower()
    to: str = to.lower()

    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    if base == 'eur':
        return amount * to_rates['rate']
    else:
        return amount * (to_rates['rate'] / from_rates['rate'])


def main() -> None:
    rates: dict[str, dict] = load_rates('rates.json')
    result: float = convert(amount=10, base='lolo', to='dkk', rates=rates)
    print(result)


if __name__ == '__main__':
    main()