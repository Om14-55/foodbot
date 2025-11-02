from setuptools import find_packages,setup

setup(
  name="FoodRecipebot",
  version="0.0.1",
  author="Rohit",
  author_email="rohit2002sha@gmail.com",
  packages=find_packages(),
  install_requires=[
        "langchain",
        "langchain-google-genai",
        "langchain-astradb",
        "datasets",
        "pypdf",
        "python-dotenv",
        "flask",
        "google-generativeai"
    ]
)