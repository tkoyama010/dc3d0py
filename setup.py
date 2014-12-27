from setuptools import setup, find_packages

setup(name='dc3d0py',
      version='0.0.1',
      description='Python wrapper for dc3d0',
      author='Tetsuo Koyama',
      author_email='tkoyama010@gmail.com',
      url='https://tkoyama010@bitbucket.org/tkoyama010/dc3d0py.git',
      packages=find_packages(),
      entry_points="""
      [console_scripts]
      greet = dc3d0py.dc3d0py:main
      """,)
