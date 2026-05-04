from setuptools import setup, find_packages

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="calorie_expenditure",
    version="0.0.1",
    author="Raksha Kadam",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)

# // To install the package, run: pip install -e .
