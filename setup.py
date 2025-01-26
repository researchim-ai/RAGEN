# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# setup.py is the fallback installation script when pyproject.toml does not work
from setuptools import setup, find_packages
import os
import sys

version_folder = os.path.dirname(os.path.join(os.path.abspath(__file__)))

with open(os.path.join(version_folder, 'verl/version/version')) as f:
    __version__ = f.read().strip()


with open('requirements.txt') as f:
    required = f.read().splitlines()
    install_requires = [item.strip() for item in required if item.strip()[0] != '#']

extras_require = {
    'test': ['pytest', 'yapf']
}

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


if '--core' in sys.argv:
    setup(
        name='verl-core',
        version=__version__,
        package_dir={'': '.'},
        packages=find_packages(include=['verl']),
        url='https://github.com/volcengine/verl',
        license='Apache 2.0',
        author='Bytedance - Seed - MLSys',
        author_email='zhangchi.usc1992@bytedance.com, gmsheng@connect.hku.hk',
        description='veRL: Volcano Engine Reinforcement Learning for LLM',
        install_requires=install_requires,
        extras_require=extras_require,
        package_data={'': ['version/*'],
                    'verl': ['trainer/config/*.yaml'],},
        include_package_data=True,
        long_description=long_description,
        long_description_content_type='text/markdown'
    )

elif '--agent' in sys.argv:
    setup(
        name='verl-agent-ext',
        version='0.1',
        packages=find_packages(include=['agent']),
        author='Zihan Wang, Manling Li, Yiping Lu',
        author_email='zihanwang.ai@gmail.com, manling.li@northwestern.edu, yiping.lu@northwestern.edu',
        acknowledgements='We thank DeepSeek for providing the DeepSeek-R1 model and ideas; we thank the authors of the original verl-core package for their work; we thank the authors of TinyZero for helping us doing the early exploration; we thank Runxin Xu for the insightful discussions.',
        description='VERL + AGENT + R1',
        install_requires=[
            'verl-core>=0.1'
        ],
        package_data={'agent': ['*/*.md']}, 
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
        ]
    )

else:
    setup(
        name='verl-full',
        packages=find_packages(include=['verl', 'agent']),
        install_requires=[
            'verl-core>=0.1',
            'verl-agent-ext>=0.1'
        ]
    )
