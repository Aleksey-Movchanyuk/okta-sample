from setuptools import setup, find_packages

setup(
    name='okta-sample-backend',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'wfastcgi==3.0.0',
        'Flask==2.2.3',
        'Flask-Cors==3.1.0',
        'okta_jwt_verifier==0.7.0'
    ],
    include_package_data=True,
    zip_safe=False,
)
