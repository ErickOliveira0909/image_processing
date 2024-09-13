from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

    with open("requeriments.txt") as f:
        requeriments = f.read().splitlines()

        setup(
            name="image_processing",
            author="Erick_Oliveira",
            author_email="erickalex0909@gmail.com",
            description="image processing",
            long_description=page_description,
            long_description_content_type="text/markdown",
            url="https://github.com/ErickOliveira0909/image_processing",
            packages=find_packages(),
            install_requires=requeriments,
        )