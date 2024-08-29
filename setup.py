# setup.py
"""
oreoptmgo: PTM analysis pipeline for ToxicoProtoemics Lab.
"""
from setuptools import find_packages, setup

setup_requires = [
    ]

install_requires = [
    'pandas>=1.5.3',
    'requests>=2.28.2',
    'scipy>=1.10.0',
    'seaborn>=0.12.2',
    'pyiptmnet>=0.1.8',
    ]

setup(
   name='oreoptmgo',
   version='0.1.0',
   author='Hyunchae Sim',
   author_email='simhc0714@gmail.com',
   packages=find_packages(include=['oreoptmgo']),
   install_requires=install_requires,
   setup_requires=setup_requires,
   )

# Package 설정
# https://velog.io/@rhee519/python-project-packaging-setuptools#getting-started
# https://data-newbie.tistory.com/770
# http://www.flowdas.com/blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-setuptools/
#
# pip install -e .
#
# Terminal Log
#
# Obtaining file:///C:/Users/user/Documents/GitHub/oreoptmgo
#   Installing build dependencies ... done
#   Checking if build backend supports build_editable ... done
#   Getting requirements to build editable ... done
#   Preparing editable metadata (pyproject.toml) ... done
# Requirement already satisfied: pandas>=1.5.3 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from oreoptmgo==0.1.0) (1.5.3)
# Requirement already satisfied: requests>=2.28.2 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from oreoptmgo==0.1.0) (2.28.2)
# Requirement already satisfied: scipy>=1.10.0 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from oreoptmgo==0.1.0) (1.10.0)
# Requirement already satisfied: seaborn>=0.12.2 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from oreoptmgo==0.1.0) (0.12.2)
# Collecting pyiptmnet>=0.1.8 (from oreoptmgo==0.1.0)
#   Downloading pyiptmnet-0.1.8-py3-none-any.whl.metadata (13 kB)
# Requirement already satisfied: python-dateutil>=2.8.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pandas>=1.5.3->oreoptmgo==0.1.0) (2.8.2)
# Requirement already satisfied: pytz>=2020.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pandas>=1.5.3->oreoptmgo==0.1.0) (2023.3)
# Requirement already satisfied: numpy>=1.21.0 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pandas>=1.5.3->oreoptmgo==0.1.0) (1.24.3)
# Requirement already satisfied: certifi in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pyiptmnet>=0.1.8->oreoptmgo==0.1.0) (2022.12.7)
# Collecting chardet (from pyiptmnet>=0.1.8->oreoptmgo==0.1.0)
#   Downloading chardet-5.2.0-py3-none-any.whl.metadata (3.4 kB)
# Requirement already satisfied: idna in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pyiptmnet>=0.1.8->oreoptmgo==0.1.0) (3.4)
# Collecting jsonschema (from pyiptmnet>=0.1.8->oreoptmgo==0.1.0)
#   Downloading jsonschema-4.23.0-py3-none-any.whl.metadata (7.9 kB)
# Requirement already satisfied: six in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pyiptmnet>=0.1.8->oreoptmgo==0.1.0) (1.16.0)
# Requirement already satisfied: urllib3 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from pyiptmnet>=0.1.8->oreoptmgo==0.1.0) (1.26.15)
# Requirement already satisfied: charset-normalizer<4,>=2 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from requests>=2.28.2->oreoptmgo==0.1.0) (3.1.0)
# Requirement already satisfied: matplotlib!=3.6.1,>=3.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from seaborn>=0.12.2->oreoptmgo==0.1.0) (3.7.1)
# Requirement already satisfied: contourpy>=1.0.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (1.0.7)
# Requirement already satisfied: cycler>=0.10 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (0.11.0)
# Requirement already satisfied: fonttools>=4.22.0 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (4.39.3)
# Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (1.4.4)
# Requirement already satisfied: packaging>=20.0 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (23.1)
# Requirement already satisfied: pillow>=6.2.0 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (9.5.0)
# Requirement already satisfied: pyparsing>=2.3.1 in c:\users\user\appdata\local\programs\python\python310\lib\site-packages (from matplotlib!=3.6.1,>=3.1->seaborn>=0.12.2->oreoptmgo==0.1.0) (3.0.9)
# Collecting attrs>=22.2.0 (from jsonschema->pyiptmnet>=0.1.8->oreoptmgo==0.1.0)
#   Downloading attrs-24.2.0-py3-none-any.whl.metadata (11 kB)
# Collecting jsonschema-specifications>=2023.03.6 (from jsonschema->pyiptmnet>=0.1.8->oreoptmgo==0.1.0)
#   Downloading jsonschema_specifications-2023.12.1-py3-none-any.whl.metadata (3.0 kB)
# Collecting referencing>=0.28.4 (from jsonschema->pyiptmnet>=0.1.8->oreoptmgo==0.1.0)
#   Downloading referencing-0.35.1-py3-none-any.whl.metadata (2.8 kB)
# Collecting rpds-py>=0.7.1 (from jsonschema->pyiptmnet>=0.1.8->oreoptmgo==0.1.0)
#   Downloading rpds_py-0.20.0-cp310-none-win_amd64.whl.metadata (4.2 kB)
# Downloading pyiptmnet-0.1.8-py3-none-any.whl (9.3 kB)
# Downloading chardet-5.2.0-py3-none-any.whl (199 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 199.4/199.4 kB 1.7 MB/s eta 0:00:00
# Downloading jsonschema-4.23.0-py3-none-any.whl (88 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 88.5/88.5 kB 5.2 MB/s eta 0:00:00
# Downloading attrs-24.2.0-py3-none-any.whl (63 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.0/63.0 kB 1.7 MB/s eta 0:00:00
# Downloading jsonschema_specifications-2023.12.1-py3-none-any.whl (18 kB)
# Downloading referencing-0.35.1-py3-none-any.whl (26 kB)
# Downloading rpds_py-0.20.0-cp310-none-win_amd64.whl (213 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 213.5/213.5 kB 3.3 MB/s eta 0:00:00
# Building wheels for collected packages: oreoptmgo
#   Building editable for oreoptmgo (pyproject.toml) ... done
#   Created wheel for oreoptmgo: filename=oreoptmgo-0.1.0-0.editable-py3-none-any.whl size=6956 sha256=2edaa239148463be28954cd18e494155a94d0408c41a787da4fd4623d52af21c
#   Stored in directory: C:\Users\user\AppData\Local\Temp\pip-ephem-wheel-cache-0woyfdzh\wheels\b1\20\bd\68b2510974e247aef4bb09b742ada5e4f5db39e06ea88acd50
# Successfully built oreoptmgo
# Installing collected packages: rpds-py, chardet, attrs, referencing, jsonschema-specifications, jsonschema, pyiptmnet, oreoptmgo
# Successfully installed attrs-24.2.0 chardet-5.2.0 jsonschema-4.23.0 jsonschema-specifications-2023.12.1 oreoptmgo-0.1.0 pyiptmnet-0.1.8 referencing-0.35.1 rpds-py-0.20.0