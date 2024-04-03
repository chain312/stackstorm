import abc
import six


# 定义基类，只包含format方法，文件路径 plugins/
@six.add_metaclass(abc.ABCMeta)
class FormatterBase(object):

    @abc.abstractmethod
    def format(self, data):
        pass
