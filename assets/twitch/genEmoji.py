import os
import yaml

import os
import yaml

def generate_yaml_data(directory, extension):
    yaml_data = []

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            name = os.path.splitext(filename)[0]
            data = {
                'name': name,
                'strings': [name],
                'location': os.path.join('assets', 'twitch', filename)
            }
            yaml_data.append(data)

    return yaml_data

def write_yaml_file(data, output_file):
    with open(output_file, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)

current_directory = os.getcwd()
file_extension = '.png'

yaml_data = generate_yaml_data(current_directory, file_extension)

output_yaml_file = 'output.yml'  # Change the extension to .yml if needed

write_yaml_file(yaml_data, output_yaml_file)

print(f'YAML file "{output_yaml_file}" created successfully.')