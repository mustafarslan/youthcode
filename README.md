# Youth Code
### Programming exercises for students

## Pre-requisites
* Python3
* PIP3
* Angular CLI
* NodeJS
* NPM
* MongoDB

## Installation
* To install client related dependencies, while you are in "client/funapp/":
  
  > npm install
  
* To install server related dependencies, while you are in "server/:

  > pip3 install -r requirements.txt
  
## To Run

Please run following command in "client/funapp":

  > npm start 

##### FAQ
* Problem with Watch functionality

  > echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
