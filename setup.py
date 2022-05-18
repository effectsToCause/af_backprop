from setuptools import setup, find_packages
setup(
    name='af_backprop',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'absl-py',
        'biopython',
        'chex',
        'dm-haiku',
        'dm-tree',
        'docker',
        'immutabledict',
        'jax',
        'ml-collections',
        'numpy',
        'pandas',
        'scipy',
        'tensorflow-cpu',
    ],
)
