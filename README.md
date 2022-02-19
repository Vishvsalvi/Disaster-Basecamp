# Disaster BaseCamp
 ## NOTE: This project has been made based on an hackathon problem statement.

1) This is a disaster management web             application written in Python-Flask.

2) In this web application users can report
 a disaster occured in their locality.
 
3) Upon reporting, a rescue team will be  informed about the situation and the location of the area affected by the disaster.

4) On the web app, guidelines have been provided for the users/visitors of the web app to promote disaster preparedness and risk reduction.


# To get the website running....

1) You should have python3 installed.
2) After cloning this repo, navigate to the repo and create a virtual environment and activate it by entering the following command in your command line:

`python3 -m venv venv_name`
### if on Mac/Linux
`source venv_name/bin/activate`
### if on windows
`venv_name\Scripts\activate`

3) Once the virtual environment is activated,
install the dependencies, you can find them in the requirements.txt file which is present in the root directory of the project, you can do by entering the following command in your command line:

`(venv_name) pip install -r requirements.txt`

4) Once all the dependencies are installed you can get the web app running, enter the following command in the root directory of your project:

`(venv_name) python app.py`

5) You can now visit the website in your browser by navigation to **http://127.0.0.1:5000/** or **http://localhost:5000/**.
6) To get mail functionality working you need to provide a dummy email and its password and also a address to send email to, you can edit the routes.py in disaster_manager package.
7) In routes.py in emergency() edit dummyemail, dummyemailpassword, and to_addr to your dummy data.
