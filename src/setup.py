from setuptools import setup
import setup_translate

pkg = 'Extensions.SetPicon'
setup(name='enigma2-plugin-extensions-setpicon',
       version='0.53',
       description='assignment picons for services',
       package_dir={pkg: 'SetPicon'},
       packages=[pkg],
       package_data={pkg: ['img/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
