Requirements:
Python3 should be installed on your pc
How to run the program:

Go to project folder where ecomenv exist, then run terminal and type: 'source ecomenv/bin/activate'

After activating virtual environment install the following libraries:
pip install psycopg2-binary
pip install pillow [for image handling]

Go to postgres-test directory and run following command:  'docker-compose up -d' 

Go to browser: localhost:8080 (if your system is using this port, update docker-compose.yml and change ports of pgadmin to different one
	       email:admin@example.com
	       password: adminpassword
	       
After you login, pgadmin will ask for postgres password, then provide it:	       
	       (I have updated on my Django settings.py file, you need not update)
	       POSTGRES DB: mydatabase
      	       POSTGRES USER: myuser
               POSTGRES PASSWORD: mypassword


On project directory, goto mysite where manage.py file exist, there you have to run terminal and type following commands:
'python3 manage.py runserver 8082'

open the browser and goto 
	localhost:8082/admin (type superadmin username and password)
		-You can add category, products and even update and delete comments of users.
	localhost:8082/products
		-There, you will find products that you have added on admin panel

Superadmin (DJango Dashboard):
		User: admin                 
		Pass: admin321@
                    


