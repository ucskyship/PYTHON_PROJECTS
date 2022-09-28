class AppException(Exception):

    def __init__(self, msg) -> None:
        super.__init__(msg)

        raise AppException("Useless exception")
