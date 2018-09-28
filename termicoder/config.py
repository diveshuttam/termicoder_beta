import click
import os
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


# TODO handle exceptions and messages in a better way
# TODO `load` and `safe_load` properly.
# In places, it may be more powerful to use load instead of safe_load
# (yaml files can call funcions if using load)

# file_path is relative to the config_path
# currently safe=True is not supported yet
# key = None return the whole config
def get_config(file_path, key=None, safe=False):
    if(safe is True):
        # use safe load later
        pass

    config_path = click.get_app_dir("termicoder")
    data_path = os.path.join(config_path, file_path)

    if(not os.path.exists(data_path)):
        msg = "Could not find config file: '{data_path}'\n".format(
            data_path=data_path) + "Run `termicoder config init` first!"
        raise click.UsageError(msg)

    data_file = click.open_file(data_path)

    try:
        data = yaml.load(data_file, Loader=Loader)
        print(data)
        if key is None:
            value = data
        else:
            value = data[key]
    except (yaml.YAMLError, KeyError):
        value = None
    return value


# if key is none, rewrite the whole file with value
def write_config(file_path, key, value):
    config_path = click.get_app_dir("termicoder")
    existing_data = get_config(file_path, None)
    if existing_data is None:
        existing_data = {}

    if key is not None:
        existing_data[key] = value
    else:
        existing_data = value

    data_file = click.open_file(os.path.join(config_path, file_path), 'w')
    try:
        yaml.dump(data=existing_data, stream=data_file, Dumper=Dumper)
    except yaml.YAMLError:
        pass


# just for testing purposes
if __name__ == "__main__":
    write_config('settings.yml', 'browser', None)
