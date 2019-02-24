**Feature Request APP**

* Steps to run the Project
  * Database Setup
    * Install Mysql and create database 
    * Go to settings file and provide database info in DATABASE
  * VirtualEnv
     * Create Virtualenvironment and activate it
     *  Install requirement/dev.txt and requirements/common.txt
        using command
        * pip install -r requirements/dev.txt and
        * pip install requirements/common.txt
   * Run migrations
        * python manage.py migrate
   * Load initial data for client table using management command
        * python manage.py load_initial_data
    
   * Run server
        * python manage.py runserver   
   
    * for running api unit test case for feature 
         * python manage.py test
 
~                              
