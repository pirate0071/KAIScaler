from setuptools import setup, find_packages

setup(
    name='kaiscaler',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'kubernetes',
        'prometheus-api-client',
        'tensorflow',
        'numpy',
        'flask',
        'joblib'
    ],
    entry_points={
        'console_scripts': [
            'kaiscaler-operator=operator.kaiscaler_operator:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.8',
)
