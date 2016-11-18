from setuptools import setup, find_packages

setup(name = "boiler-controller",
      version ="0.7dev",
      description='',
      author = "Kateřina Kratochvílová,Jan Kohlíček",
      author_email = "dtwok8@students.zcu.cz,kohl@students.zcu.cz",
      url = 'https://github.com/dtwok8/TI-boiler-controller',
      license = 'BSD',
      packages = find_packages(exclude=['tests', 'tests.*'])
      #entry_points = {'console_scripts' : {'main = '}}
      )
