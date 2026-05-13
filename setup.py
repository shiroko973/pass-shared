import os
from setuptools import setup

setup(
    name='pass-shared',
    version='2.0.0',
    author='Rim Valiulin, shiroko',
    author_email='rim.valiulin@gmail.com, 3207774253@qq.com',
    url='https://github.com/shiroko973/pass-shared',
    download_url='https://github.com/shiroko973/pass-shared',
    license='BSD',
    description='CSS preprocessor (Python 3 port of the original Pass by Rim Valiulin)',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=['pass_shared'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    python_requires='>=3.6',
)