from setuptools import setup, find_packages

setup(
    name="mcq-generator",
    version="0.1.0",
    author="Laya Krishna Kalwa",
    author_email="layakrishnakalwa@gmail.com",
    description="AI-powered MCQ Generator using Bolt IoT AI",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "boltiotai",
        "langchain",
        "streamlit",
        "python-dotenv",
        "PyPDF2",
    ],
)
