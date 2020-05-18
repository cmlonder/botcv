# Run
Before starting you should run Appium server. You can use [Appium Desktop](https://github.com/appium/appium-desktop)
which has also good inspector that helps you interact with your phone. Also you can run lightweight 
[Appium Server](http://appium.io/docs/en/about-appium/getting-started/?lang=tr) directly.

# Development
To start working as a developer, follow steps
## Enable Venv
1. invoke venv which creates necessary folder
    ```
    python -m venv venv/
    ```
2. then activate (for windows)
    ```
    venv\Scripts\activate
    ```
   
3. you can deactivate it as follows:
    ```
    venv\Scripts\deactivate
    ```
   
Resource [here](https://docs.python.org/3/library/venv.html)

## Install Dependencies
After venv is enabled, install reqired dependencies:

```
pip install -r requirements.txt
```

## Save Dependencies
Whenever you install dependencies you can save them to requirements.txt
as follows:
first install your required dependency
```
pip install ${YOUR_PACKAGE}
```

Then save it to requirements.txt
```
pip freeze > requirements.txt
```

## Install and Save
To not forget to save dependencies to requirements.txt you can install
and save at the same time:

```
pip install ${YOUR_PACKAGE} && pip freeze > requirements.txt
```

## Set Code Formatter
We are using [Black](https://github.com/psf/black) as code formatter. Follow instructions to set your IDE/environment to auto format on save.
[Here](https://github.com/psf/black#pycharmintellij-idea) is the instructions for PyCharm.




