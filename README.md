# Data Analyst Challenge - friendsuarnce

## Overview

This repository contains code to load data into a ```postgres``` database from ```CSV``` files.  The data is loaded into ```PUBLIC.CUSTOMER```, ```PUBLIC.EXCHANGE_RATE``` and ```PUBLIC.TRANSACTION_DETAIL``` tables via insert else update load strategy from the ```customer.csv```, ```exchange_rate.csv``` and ```transaction.csv``` files, respectively. The challenge overview is available [here](docs/challenge.md).

## Steps

**Prerequisites**
1.	Download the GitHub Repository: The whole file can be downloaded as a zip 

2.	Extract & Navigate to Project Directory: In my case, I have Ubuntu as the virtual system and the below codes are for the same.

  	 ```cd friendsurance_challenge_marzooqe-main```
  	
4.	(Optional) Open project in Visual Studio Code

    ```code .```
   
**Implementation**
1. Define user environment variables inside ```.env``` after copying example environment file, ```env.example```, as ```.env```. The ```.env``` file will contain sensitive information like username, password, API Key etc.

    ```cp env.example .env```

2. Create a virtual environment, named as ```venv```.

    ```python3 -m venv venv```

3. Activate the created virtual environment

    ```source ./venv/bin/activate```

4. Install the required libraries and dependencies from ```requirements.txt```

    ```pip install -r requirements.txt```
   
5. Run the docker container for running ```postgres:15-alpine``` database an ```pgadmin``` services.

    ```docker-compose up```

6. Run the python script to run the required data pipelines.

    ```python3 main.py```

8. Install these libraries incase the requirement file has exception or error

    ```pip install psycopg2-binary```
    ```pip install sqlalchemy```
    ```pip install dotenv```

