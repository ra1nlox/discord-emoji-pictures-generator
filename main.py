import configparser
import click

config = configparser.ConfigParser()
config.read("config.ini")
config.set('settings', 'rows', '7')
config.set('settings', 'length', '7')

outfile = open('output.txt', 'a')

emoji0 = config["emojis"]["emoji0"]
emoji1 = config["emojis"]["emoji1"]
emoji2 = config["emojis"]["emoji2"]
emoji3 = config["emojis"]["emoji3"]
emoji4 = config["emojis"]["emoji4"]
emoji5 = config["emojis"]["emoji5"]
emoji6 = config["emojis"]["emoji6"]
emoji7 = config["emojis"]["emoji7"]
emoji8 = config["emojis"]["emoji8"]
emoji9 = config["emojis"]["emoji9"]

max_rows = config['settings']['rows']
max_length = config['settings']['length']

@click.group()
def cli():
	pass

"""@cli.command()
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
		print('Error: "number" is bigger than 8')"""

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
	elif number == 4:
		config.set('emojis', 'emoji4', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	elif number == 5:
		config.set('emojis', 'emoji5', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	elif number == 6:
		config.set('emojis', 'emoji6', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	elif number == 7:
		config.set('emojis', 'emoji7', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	elif number == 8:
		config.set('emojis', 'emoji8', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	elif number == 9:
		config.set('emojis', 'emoji9', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	elif number == 10:
		config.set('emojis', 'emoji10', str(name0))
		with open("config.ini", 'w') as config_file:
			config.write(config_file)
	else:
		print("Error: wrong number")

@cli.command()
def set_shape():
	row0 = input("(Use numbers from 0 to 9 where you need a emoji, split it with a just space)\nFirst row: ")
	row1 = input("Second row: ")
	row2 = input("Third row: ")
	row3 = input("Fourth row: ")
	row4 = input("Fifth row: ")
	row5 = input("Sixth row: ")
	row6 = input("Seventh row: ")
	row_all = f'{row0}\n{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}'
	config.set('shape', 'shape', str(row_all))
	with open("config.ini", 'w') as config_file:
		config.write(config_file)

@cli.command()
def generate():
	shape = config['shape']['shape']
	final_form = shape.replace('0', emoji0)
	final_form = final_form.replace('1', emoji1)
	final_form = final_form.replace('2', emoji2)
	final_form = final_form.replace('3', emoji3)
	final_form = final_form.replace('4', emoji4)
	final_form = final_form.replace('5', emoji5)
	final_form = final_form.replace('6', emoji6)
	final_form = final_form.replace('7', emoji7)
	final_form = final_form.replace('8', emoji8)
	final_form = final_form.replace('9', emoji9)
	final_form = final_form.replace(' ', '')
	print(final_form)
	with outfile as of:
		of.write('\n')
		of.write('Output:')
		of.write('\n')
		of.write(final_form)
		of.write('\n')
		of.close()


"""@cli.command()
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
		print(max_length)"""

if __name__ == '__main__':
	cli()