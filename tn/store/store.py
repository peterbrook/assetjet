# base store class
class Store():

    OfType=None

    def __init__(self, modelType=None):
        self.OfType = modelType
        try:
            self.conn = get_connection()
        except Exception as e:
            raise StoreException(*e.args, **e.kwargs)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        # can test for type and handle different situations
        self.close()

    def complete(self):
        self._complete = True

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                raise StoreException(*e.args)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    raise StoreException(*e.args)


# store for User obects
class UserStore(Store):

    def add_user(self, user):
        try:
            c = self.conn.cursor()
            # this needs an appropriate table
            c.execute('INSERT INTO user (name) VALUES(?)', (user.name,))
        except Exception as e:
            raise StoreException('error storing user')
