from setuptools import setup, find_packages

requirements = [
    'ballet>=0.5.1',
    'Click>=6.0',
]

setup(
    author='Kelvin Lu',
    author_email='kelvinlu@mit.edu',
    entry_points={
        'console_scripts': ['ballet_ames_sim_lower_threshold-engineer-features=ballet_ames_sim_lower_threshold.features:main'],
    },
    install_requires=requirements,
    name='ballet_ames_sim_lower_threshold',
    packages=find_packages(include=['ballet_ames_sim_lower_threshold', 'ballet_ames_sim_lower_threshold.*']),
    url='https://github.com/kelvin-lu/ballet_ames_sim_lower_threshold',
)
