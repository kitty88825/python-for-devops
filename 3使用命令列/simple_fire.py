'''
Need pip install fire

簡單的 fire 範例
'''
import fire


def greet(greeting='Hiya', name='Tammy'):
    print(f'{greeting} {name}')


def goodbye(goodbye='Bye', name='Tammy'):
    print(f'{goodbye} {name}')


if __name__ == '__main__':
    fire.Fire()
