import fire
import pkgutil
import importlib


def find_and_run_plugins(plugin_prefix):
    plugins = {}

    # 探索並且載入外掛
    print(f'Discovering plugins with prefix: {plugin_prefix}')
    for _, name, _ in pkgutil.iter_importer_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    # 執行外掛
    for name, module in plugins.items():
        print(f'Running plugin {name}')
        module.run()


if __name__ == '__main__':
    fire.Fire()
