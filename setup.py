
# -*- coding: utf-8 -*-
from setuptools import setup

import codecs

with codecs.open('README.md', encoding="utf-8") as fp:
    long_description = fp.read()
INSTALL_REQUIRES = [
    'nonebot2>=2.0.0b4',
    'nonebot-adapter-onebot>=2.1.3',
    'numpy>=1.23.3',
    'playwright>=1.26.1',
]

setup_kwargs = {
    'name': 'nonebot_plugin_ykt',
    'version': '0.1.5',
    'description': '一个基于nonebot的雨课堂自动签到插件',
    'long_description': long_description,
    'license': 'MIT',
    'author': '',
    'author_email': 'sena-nana <851183156@qq.com>',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': [
        'nonebot-plugin-ykt',
        'build.lib.nonebot-plugin-ykt',
        'build.lib.build.lib.nonebot-plugin-ykt',
        'build.lib.build.lib.build.lib.nonebot-plugin-ykt',
        'build.lib.build.lib.build.lib.build.lib.nonebot-plugin-ykt',
        'nonebot-plugin-ykt.utils',
    ],
    'package_data': {'': ['*']},
    'long_description_content_type': 'text/markdown',
    'install_requires': INSTALL_REQUIRES,
    'python_requires': '>=3.10',

}


setup(**setup_kwargs)
