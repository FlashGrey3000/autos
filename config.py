from configparser import ConfigParser

def load_configs(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    if parser.has_section(section):
        config = {}

        for k,v in parser.items(section):
            config[k] = v
        
        return config
    else:
        raise Exception(f"No section {section} in file {filename}")

if __name__ == "__main__":
    configs = load_configs()
    print(configs)