from setuptools import setup, find_packages

setup(
    name='word_cloud',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'word_cloud=word_cloud.word_cloud:main',
        ],
    },
    install_requires=[
        'matplotlib',
        'nltk',
        'wordcloud',
        'PyPDF2',
        'textract',
        'numpy',
        'argparse',
        'Pillow',
    ],
)
