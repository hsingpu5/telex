import os,sys
ret = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ret)

from lib.conf import settings
from lib.import_string import get_class


def run():
    """程序的入口"""


    print('执行内容')
    # class_path = settings.ENGINE_DICT.get(settings.ENGINE)  # 'src.engine.agent.AgentHandler',
    #
    # # 'src.engine.agent'  'AgentHandler'
    # cls = get_class(class_path)
    # obj = cls()
    # obj.handler()
