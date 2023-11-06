from setuptools import setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="batchalier",
    version="0.0.1",
    description="Convienient micro-batching jobs via a kafka bus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Bergamin",
    author_email="daniel@bergam.in",
    license="MIT",
    keywords="batching microbatching job",
    url="http://github.com/dbergamin/batchalier",
    packages=["batchalier"],
    package_data={"": ["py.typed"]},
    python_requires=">=3.11",
    install_requires=[
        "requests",
        "confluent_kafka",
    ],
    extras_require={
        "dev": ["black", "flake8", "isort", "mypy", "pylint", "pytest"],
    },
)
