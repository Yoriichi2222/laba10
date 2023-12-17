import typer

import random_num_gen
import function
import calculator

app = typer.Typer()


@app.command()
def ca_lc(operator: str, initial: int):
    print(f'operator: {operator}, initial: {initial}\n', calculator.make_calc(operator, initial))


@app.command()
def foo(n: int):
    print(f'n: {n}\n', function.calculate_xi(n))


@app.command()
def rand(min_val: int, max_val: int):
    print(f'min_value: {min_val}, max_value: {max_val}\n', random_num_gen.generate_random_number(min_val, max_val))


if __name__ == "__main__":
    app()
