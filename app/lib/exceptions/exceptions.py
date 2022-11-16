# app/lib/mortgage/exceptions.py


class BaseMotimaticException(Exception):
    def __init__(self, name: str):
        self.name = name


class ServerError(BaseMotimaticException):
    pass


class DatabaseError(ServerError):
    pass


class TooManyMatchingRecords(DatabaseError):
    pass


class NoMatchingRecordFound(DatabaseError):
    pass


class NoResultSetProducedByQuery(DatabaseError):
    pass


class DataLookupError(DatabaseError):
    pass
