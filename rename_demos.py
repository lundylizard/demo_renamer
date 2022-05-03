import os

print('Made by lundylizard\n')
for file in os.listdir('./'):

    if file != 'rename_demos.py':
        new_filename = './' + file.replace(file.split('_')[0], str(int(file.split('_')[0]) + 1)).replace('.dem', '') + '.dem '
        os.rename('./' + file, new_filename)
        print('./' + file, '\t->\t', new_filename)

os.system('pause')
