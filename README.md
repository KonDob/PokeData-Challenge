# [PokeData Challenge](https://github.com/KonDob/PokeData-Challenge)


## Preview
This is description of PokeData project. 

## Download and Installation

You can download the project via link https://github.com/KonDob/PokeData-Challenge.
Repo is public.

## Usage
1) Open PokeData folder in console. 
2) To install all necessary packages run command "pip install -r requirements.txt"
3) For precise result - run command one by one within order from Implemented Test Tasks topic.

## Implemented Test Tasks
1) Task 1: Data Extraction - is implemented in data_extracting.py file. 
    To run in - run command 'python data_extracting_new.py' in console.
    It will create a file pokemon.csv with required data and print items.
   
2) Task 2: Data Transformation with Apache Beam.
    To see result of this task run in the console : python data_transformation.py.
   
3) Task 3: Data Loading.
    I implement loading data into the table as the step of pipeline in data_transformation.py file.
   To get result run 'python data_extracting_new.py' in console.
   For that I created separate file db_operations.py for better code design. And decided
   to create a DB there.
    
4) Task 4: Extra Feature - Advanced Data Processing.
    To see the average and max BMI run command 'python db_operations.py'
    
5) Task 5: Data Visualization.
    Run command in terminal 'python data_visualization.py' to see plots.
    
## Ideas to improve

Data extracting : it`s better to use JSON. But I"d faced with some  unclear
issue with readFromJson method in apache_beam package. 
There is few more ways to print the transformed data from Task 2. I choose to print
items in the pipeline such like : using DB query(SELECT * ...) etc.
Also DB operations can be in other place, not together with DB classes.
About 5 tasks - I decided to show 2 graphics together. It is easier to analyze them.


## About

Test tasks implemented by Konstantin. For questions or suggestion write me to :
email : konstantin.dobro@gmail.com