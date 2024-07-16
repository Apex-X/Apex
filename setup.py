import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apexx",
    version="0.0.1",
    author="Nima Mashhadi M. Reza",
    author_email="n.twenty.five.a@gmail.com",
    description="Apex-x is a project to create a new project by using a blueprint for ANY LANGUAGE!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n25a/Apex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "asgiref==3.8.1",
        "certifi==2024.6.2",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "Django==4.2.13",
        "django-emoji==2.2.2",
        "emoji==2.12.1",
        "idna==3.7",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "Pygments==2.18.0",
        "requests==2.32.3",
        "rich==13.7.1",
        "shellingham==1.5.4",
        "sqlparse==0.5.0",
        "tqdm==4.66.4",
        "typer==0.12.3",
        "typing_extensions==4.12.2",
        "urllib3==2.2.2",
    ],
    python_requires='>=3.7',
)
