def config_parser(config_path):
    with open(config_path, 'r') as conf_files:
        config = dict()
        lines = conf_files.readlines()
        for line in lines:
            k,v = line.split(' = ')
            config[k] = v
        return config