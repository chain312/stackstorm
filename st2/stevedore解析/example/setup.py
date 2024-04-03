from setuptools import setup, find_packages
setup(
    name="demo",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'stevedore.formatter': [
            'simple = plugins.simple:Simple',
            'plain = plugins.simple:Simple',
        ],
    },
)
