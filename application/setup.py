from setuptools import setup

setup(
    name='application',
    packages=['sommelier'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
