import json


def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base: str = input('What currency are we looking at: ').lower()
    while base not in rates:
        print('You must choose one of the rates: ')
        print(rates.keys())
        base: str = input('What currency are we looking at: ').lower()

    to: str = input('To what currency are we converting: ').lower()
    while to not in rates:
        print('You must choose one of the rates: ')
        print(rates.keys())
        to: str = input('So whats the target currency? : ').lower()

        from_rates: dict | None = rates.get(base)
        to_rates: dict | None = rates.get(to)

    if base == 'eur':
        return amount * to_rates['rate']
    else:
        return amount * (to_rates['rate'] / from_rates['rate'])


def main() -> None:
    rates: dict[str, dict] = load_rates('rates.json')
    result: float = convert(amount=10, base='PAB', to='dkk', rates=rates)
    print(result)


if __name__ == '__main__':
    main()