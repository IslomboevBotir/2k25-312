class Config:
    _instance = None

    def __init__(self):
        if Config._instance is not None:
            raise Exception('Config sinfi singleton bo`lishi kerak')
        self.env = 'development'
        self.log_level = 'INFO'

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Config()
        return cls._instance
