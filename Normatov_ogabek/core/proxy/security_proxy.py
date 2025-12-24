class SecurityProxy:
    def __init__(self, real_security):
        self._real = real_security
        self._auth_token = None

    def authenticate(self, token):
        # simple check
        self._auth_token = token

    def perform_check(self, level):
        if self._auth_token != 'admin-token':
            print('[Proxy] Unauthorized access attempt recorded')
            return False
        return self._real.perform_check(level)

    def status(self):
        return self._real.status()
