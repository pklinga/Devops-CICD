with open('boiler.html', 'r') as boilerplate:
    boiler_list = boilerplate.readlines()
    list_one = boiler_list[:13]
    list_two = boiler_list[14:]

with open('output.txt', 'r') as output_file:
    output_list = output_file.read().splitlines()

with open('output/index.html', 'a') as boiler_file:
    for line in list_one:
        boiler_file.write(line)
    for i in output_list:
        boiler_file.write(f'\t\t<li>{i}</li>\n')
    for line in list_two:
        boiler_file.write(line)
