# 生产时环境

import os
pre_path = os.path.dirname(os.path.realpath(__file__))
os.system('python {}/manage.py runserver 0.0.0.0:80'.format(pre_path))

