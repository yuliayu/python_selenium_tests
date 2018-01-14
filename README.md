**Technology stack:**

Selenium webdriver , python, pytest
Tested on Python 3.5.1, pytest 3.3.2, Firefox 57.0.4 , selenium 3.8.1
        
**Usage:**

1. Clone the project locally: git clone
2. Install Python 3.5
3. Install Selenium webdriver components
4. Install Firefox 57.0.4 or higher 
5. Install geckodriver and add it to the system $PATH 
6. Install pytest and setup tools : "pip3 install -U pytest", "pip3 install -U setuptools" (install pip if required)
7. Open a command prompt, make sure that you are located in a project folder and enter:
_"python3 -m pytest --junitxml=report.xml"_

**Report:**
Test report would be generated after the execution and could be found in a root folder in file "report.xml" 