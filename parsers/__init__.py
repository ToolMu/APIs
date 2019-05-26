# Yaml文件处理器
import six

from abc import ABCMeta, abstractmethod


@six.add_metaclass(ABCMeta)
class Parser:
    @abstractmethod
    def parser(self, file_path):
        pass
