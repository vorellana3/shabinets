from setuptools import setup

setup(
    name='shabinets',
    version='1.0',
    description='Not so shabby food inventory management',
    author='Sean Aoki, Nithya Jayakumar, Vivien Orellana, Holden Rohrer',
    packages=['shabinets'],
    install_requires=['pandas', 'numpy', 'Flask', "mysql-connector-python", "python-dotenv", "flask-cors"],
)
