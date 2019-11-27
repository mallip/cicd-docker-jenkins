from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.0",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = [
		 	   "Django>=1.9,<2.0",
			   "django-cors-headers>=3.0.2",
			   "djangorestframework>=3.9.4",
			   "dnspython>=1.16.0",
			   "mysql-connector-python>=8.0.18",
			   "mysqlclient>=1.4.6",
			   "protobuf>=3.10.0",
			   "PyMySQL>=0.9.3",
			   "pytz>=2019.3" ],
  extras_require       = {
                            "test": [
				"colorama>=0.4.1",
				"coverage>=4.5.4",
				"django-nose>=1.4.6",
				"nose>=1.3.7",
				"pinocchio>=0.4.2"
                            ]
                         }
)
