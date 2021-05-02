import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="owm-api-mugan86",
    version="0.0.1",
    author="Anartz Mugika Ledo",
    author_email="mugan86@gmail.com",
    description="Obtener la información del tiempo actual y previsión con Openweather Map Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mugan86/<mi-proyecto>",
    project_urls={
        "Bug Tracker": "https://github.com/mugan86/<mi-proyecto>/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)