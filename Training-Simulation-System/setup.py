from setuptools import setup, find_packages

setup(
    name='training_simulation_system',
    version='1.0.0',
    author='ParaCryptid',
    description='Secure cross-platform training simulation system',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'flask',
        'pyyaml',
        'requests',
        'rich',
        'loguru'
    ],
    entry_points={
        'console_scripts': [
            'simulator=main:main'
        ]
    },
)