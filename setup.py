from setuptools import find_packages, setup

setup(
    name="delta_env",
    version="0.1.0",
    author="Cetin Alanyalioglu",
    author_email="cetinalanyalioglu@gmail.com",
    description="A simple tool to analyze how a shell script modifies environment variables",
    packages=find_packages(),
    python_requires=">=3.0.0",
    entry_points={"console_scripts": ["delta-env=delta_env.cmd:delta_env_command_line"]},
)
