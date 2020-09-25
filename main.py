import configparser
import click

config = configparser.ConfigParser()
config.read("config.ini")

outfile = open('output.txt', 'a')

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
	if number <= 8:
		config.set('settings', 'rows', str(number))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	else:
		print('Error: "number" is bigger than 8')

@cli.command()
@click.option('-n', '--number', nargs=1, type=int)
def set_length(number):
	if number <= 8:
		config.set('settings', 'length', str(number))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	else:
		print('Error: "number" is bigger than 8')

@cli.command()
@click.option('-n', '--number', nargs=1, type=int, help='Number of emoji')
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


@cli.command()
def generate_square7():
	if int(max_length) <= 7 and int(max_rows) <= 7:
		row0 = emoji1*7
		row1 = emoji1*2 + emoji2*3 +emoji1*2
		row2 = emoji1 + emoji2 + emoji1*3 + emoji2 + emoji1
		row3 = emoji1 + emoji2 + emoji1*3 + emoji2 + emoji1
		row4 = emoji1 + emoji2 + emoji1*3 + emoji2 + emoji1
		row5 = emoji1*2 + emoji2*3 +emoji1*2
		row6 = emoji1*7

		with outfile as of:
			of.write('\n')
			of.write('Output:')
			of.write('\n')
			of.write(row0)
			of.write('\n')
			of.write(row1)
			of.write('\n')
			of.write(row2)
			of.write('\n')
			of.write(row3)
			of.write('\n')
			of.write(row4)
			of.write('\n')
			of.write(row5)
			of.write('\n')
			of.write(row6)
			of.write('\n')
			of.close()

	else:
		print("Error: 'length' is too big")
		print(max_length)

if __name__ == '__main__':
	cli()