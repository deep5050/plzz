plzz --develop
python3 setup.py build
sudo python3 setup.py install

python setup.py sdist clean
python setup.py sdist bdist_wheel

twine check dist/*
twine upload dist/* --verbose