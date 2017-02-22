import os
from setuptools import (
    setup,
    find_packages,
)

setup(
    name='FDA Transportal',
    version='0.9',
    long_description="A portal of transporters",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'transportal-manage = transportal:manage',
        ]
    },
    include_package_data=True,
    package_data={
        'initial-data': 'transportal/initial_data.json',
        'database': 'transportal/fdaTransporter.sqlite',
        'templates': 'transportal/templates/*',
        'media': 'transportal/media/*',
        'requirements': 'requirements.txt',
    },
    zip_safe=False,
    install_requires=[
        'django',
    ],
    classifiers=[
        'Private :: Do Not Upload',
    ]
)
