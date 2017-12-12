import configparser
config = configparser.ConfigParser()
config.read('events.ini')

eps = float(config['DEFAULT']['events_per_sec'])

sleep_time  = 1.0/eps
print sleep_time
