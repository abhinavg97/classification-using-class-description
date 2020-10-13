import json
from logger.logger import logger

global seed
seed = 0

global configuration
configuration = {

    "DEBUG":    True,

    # These paths are relative to the main directory
    "paths":        {
        'data_root':  "data/",
        "output":    "output/",
        "log":       "logs/",
        "dataset":  "data.txt",
        "labels": "labels/"
    },

    "data":         {
        "num_workers": 4,
        "dataset":     {
            'name': 'custom'
        },
        "trainval_test_split": 0.3,
        "train_val_split":  0.3,
    },
}


class Config(object):
    """ Contains all configuration details of the project. """

    def __init__(self):
        super(Config, self).__init__()

        self.configuration = configuration

    def get_config(self):
        return self.configuration

    def print_config(self, indent=4, sort=True):
        """ Prints the config. """
        logger.info("[{}] : {}".format("Configuration",
                                       json.dumps(self.configuration,
                                                  indent=indent,
                                                  sort_keys=sort)))

    @ staticmethod
    def get_platform():
        """ Returns dataset path based on OS.

        :return: str
        """
        import platform

        if platform.system() == 'Windows':
            return platform.system()
        elif platform.system() == 'Linux':
            return platform.system()
        else:  # OS X returns name 'Darwin'
            return "OSX"

    @ staticmethod
    def get_username():
        """
        :returns the current username.

        :return: string
        """
        try:
            import os
            import pwd
            username = pwd.getpwuid(os.getuid()).pw_name

        except Exception:
            import getpass

            username = getpass.getuser()
        finally:
            username = os.environ.get('USER')

        return username


config_cls = Config()
config_cls.print_config()

global platform
platform = config_cls.get_platform()
global username
username = config_cls.get_username()
