from setuptools import setup


setup(
    name='sales',
    version='0.1',
    py_modules=['sales'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sales=sales:cli
    ''',
)