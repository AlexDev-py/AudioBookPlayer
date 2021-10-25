import typing as ty
from abc import abstractmethod

from PyQt5.QtCore import QObject, QThread


class Cache(object):
    """
    Кэш.
    Временно хранит до 4-х объектов.
    """

    def __init__(self):
        self.storage = {}

    def get(self, key: str) -> ty.Any:
        """
        :param key: Ключ к объекту.
        :return: Объект.
        """
        return self.storage.get(key)

    def set(self, key: str, obj: ty.Any) -> None:
        """
        Добавляет объект в кэш.
        :param key: Ключ.
        :param obj: Объект.
        """
        if len(self.storage) >= 4:
            del self.storage[list(self.storage.keys())[0]]
        self.storage[key] = obj


class BaseWorker(QObject):
    def __new__(cls, *args, **kwargs):
        self = super(BaseWorker, cls).__new__(cls, *args, **kwargs)
        self.__init__(*args, **kwargs)
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.worker)
        return self

    @abstractmethod
    def worker(self) -> None:
        pass

    @abstractmethod
    def connectSignals(self) -> None:
        pass

    def start(self) -> None:
        self.connectSignals()
        self.thread.start()


def convert_into_seconds(seconds: int) -> str:
    """
    :param seconds: Число секунд.
    :return: Строка вида `<часы>:<минуты>:<секунды>`.
    """
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    return ((str(h).rjust(2, "0") + ":") if h else "") + ":".join(
        map(lambda x: str(x).rjust(2, "0"), (m, s))
    )


def convert_into_bits(bits: int) -> str:
    """
    :param bits: Число битов.
    :return: Строка вида <Число> <Единица измерения>
    """
    postfixes = ["КБ", "МБ", "ГБ"]
    if bits >= 2 ** 33:
        return f"{round(bits / 2 ** 33, 3)} {postfixes[-1]}"
    elif bits >= 2 ** 23:
        return f"{round(bits / 2 ** 23, 2)} {postfixes[-2]}"
    elif bits >= 2 ** 13:
        return f"{round(bits / 2 ** 13, 1)} {postfixes[-3]}"