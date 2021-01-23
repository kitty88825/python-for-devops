'''
Command-line tool using argparse
'''
import argparse


def sail():
    ship_name = 'Your ship'
    print(f'{ship_name} is setting sail')


def list_ships():
    ships = ['John B', 'Yankee Clipper, Pequod']
    print(f'Ships: {", ".join(ships)}')


def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)


if __name__ == '__main__':
    # 建立最頂層的解析器
    parser = argparse.ArgumentParser(description='Maritime control')
    # 增添最頂層的引數，該引數會屬於它的子指令一起被使用
    parser.add_argument(
        '--twice',
        '-t',
        help='Do it twice',
        action='store_true',
    )
    # 建立一個子解析器的存放物件。dest 屬性是用來判斷哪個子解析器正在被使用
    subparsers = parser.add_subparsers(dest='func')
    # 為 ships 新增子解析器
    ship_parser = subparsers.add_parser('ships', help='Ship related commands')
    # 為 ships 子解析器新增指令。 choices 參數為可使用的指令選項列表
    ship_parser.add_argument('command', choices=['list', 'sail'])
    # 為 sailors 新增子解析器
    sailor_parser = subparsers.add_parser('sailors', help='Talk to a sailor')
    # 為 sailors 子解析器添加位置相依的指令
    sailor_parser.add_argument('name', help='Sailors name')
    sailor_parser.add_argument(
        '--greeting',
        '-g',
        help='Greeting',
        default='Ahoy there',
    )

    args = parser.parse_args()
    # 透過 func 確認哪個子解析器正被使用
    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()
