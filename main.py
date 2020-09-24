import configparser
import click

config = configparser.ConfigParser()
config.read("config.ini")

emoji1 = config["emojis"]["emoji1"]
emoji2 = config["emojis"]["emoji2"]
emoji3 = config["emojis"]["emoji3"]

max_rows = config['settings']['rows']
max_length = config['settings']['length']

first = ''
second = ''
third = ''

@click.group()
def cli():
	pass

@cli.command()
@click.option('-n', '--number', nargs=1, type=int)
def set_rows(number):
    config.set('settings', 'rows', str(number))
    with open("config.ini", 'w') as config_file:
        config.write(config_file)

@cli.command()
@click.option('-n', '--number', nargs=1, type=int)
def set_length(number):
    config.set('settings', 'length', str(number))
    with open("config.ini", 'w') as config_file:
        config.write(config_file)

@cli.command()
@click.option('-n', '--number', nargs=1, type=int, help='Number of ')
@click.argument('name')
def set_emoji(number, name):
    name0 = f':{name}:'
    if number == 1:
        config.set('emojis', 'emoji1', str(name0))
        with open("config.ini", 'w') as config_file:
           config.write(config_file)
    elif number == 2:
        config.set('emojis', 'emoji2', str(name0))
        with open("config.ini", 'w') as config_file:
            config.write(config_file)
    elif number == 3:
        config.set('emojis', 'emoji3', str(name0))
        with open("config.ini", 'w') as config_file:
            config.write(config_file)

if __name__ == '__main__':
    cli()