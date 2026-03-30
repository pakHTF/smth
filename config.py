import json
def load_config(filename='config.json'):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'file {filename} is not found.')
        return None
    except json.JSONDecodeError:
        print(f'reading error.')
        return None
def save_config(config,filename='config.json'):
    with open(filename, 'w',encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, intend=4)
    print('saved settings')
def display_config(config):
    print(f"theme:{config['theme']}, font size:{config['font_size']}, language:{config['language']}")
def update_config(config):
    print('available parameters: theme, font_size, language')
    param=input('which parameter you want to tweak?').strip().lower()
    if param not in config:
        print('wrong parameter name.')
        return False
    new_value=input('insert new parameter value').strip()
    if param=="font_size":
        try:
            new_value=int(new_value)
        except ValueError:
            print('error. font_size must be an integer')
            return False
    config[param]=new_value
    print(f'parameter {param} is refreshed.')
    return True
def main():
    config=load_config()
    if config is None:
        default_config={
            'theme': 'dark',
            'font_size': 14,
            'language': 'ru'
        }
        save_config(default_config)
        config=default_config
    display_config(config)
    while True:
        if update_config(config):
            display_config(config)
            save_config(config)
        again=input("\ndo you want to change another parameter? (y/n)").strip().lower()
        if again not in ('yes', 'y'):
            break
if __name__=='__main__':
    main()
