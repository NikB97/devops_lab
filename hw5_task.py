"""HW5"""
# pylint: disable=invalid-name
import json
import sys
import os
import site
import pip
import yaml

# choice of output
print("Select the output file type(json/yaml):")
output_f = input()

# "installed packages" variable
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])


class info_python:
    """info_python class"""

    def metrics(self):
        """metrics"""
        self.version = str(sys.version)
        self.virt_env = str(sys.prefix)
        self.exec_loc = str(sys.executable)
        self.pip_loc = str(pip.__path__)
        self.path = str(os.environ['PATH'])
        self.inst_pack = str(installed_packages_list)
        self.pack_loc = str(site.getsitepackages())

    def creating_json(self):
        """json"""
        self.metrics()
        data = {"1)version": str(self.version), "2)virtual environment": str(self.virt_env), "3)python executable location": str(self.exec_loc), "4)pip location": self.pip_loc, "5)PYTHONPATH": str(self.path), "6)installed packages": str(self.inst_pack), "7)site-packages location": str(self.pack_loc)}
        with open("info_python.json", "w") as js:
            json.dump(data, js, sort_keys=True, indent=4, ensure_ascii=False)
            js.write("\n")
        print("json file created")

    def creating_yaml(self):
        """yaml"""
        self.metrics()
        data = {"1)version": str(self.version), "2)virtual environment": str(self.virt_env), "3)python executable location": str(self.exec_loc), "4)pip location": str(self.pip_loc), "5)PYTHONPATH": str(self.path), "6)installed packages": str(self.inst_pack), "7)site-packages location": str(self.pack_loc)}
        with open("info_python.yaml", "w") as ya:
            yaml.dump(data, ya, default_flow_style=False)
            ya.write("\n")
        print("yaml file created")


obj = info_python()
if output_f == "json":
    obj.creating_json()
elif output_f == "yaml":
    obj.creating_yaml()
else:
    print("incorrect input(should be JSON or YAML), run the script again !")
