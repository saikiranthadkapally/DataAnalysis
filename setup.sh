#In this we can set environment variables and Paths etc.. using shell scripting 

#NOTE:The purpose of setup.sh and config.py files can be different depending on the specific context in which they are used. However, generally speaking:

#setup.sh is a shell script file that is often used in the context of software development and deployment to set up the environment and configure the system. This file 
#can contain commands that set environment variables, add directories to the path, install packages, and perform other system-level operations.

#config.py is a Python script file that is often used to store configuration settings and parameters for a Python application. This file can contain variables and values
#that are used by the application to customize its behavior and functionality.

#The main difference between the two files is that "setup.sh" is typically used to set up the environment and configure the system, while "config.py" is used to configure 
#the application itself. setup.sh is often used as part of the installation or deployment process, while config.py is typically used by the application during runtime.

#In summary, setup.sh is used to set up the system environment and config.py is used to configure the application. They serve different purposes and are used in 
#different contexts, but both can be used to customize and control the behavior of a software system.

#We can set Python path in this file
export PYTHONPATH="$PWD:$PYTHONPATH"

#If We want to use anything as  "Environment Variables" in our Project then we declare that "Environment Variables" in this files.
ENV="STAGE"


