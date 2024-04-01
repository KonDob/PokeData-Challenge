# [PokeData Challenge](https://github.com/KonDob/PokeData-Challenge)


## Preview
This is descripton of PokeData project. 

## Download and Installation

You can download the project via link https://github.com/KonDob/PokeData-Challenge.
Repo is public.

## Usage
1) Open PokeData folder in console. 
2) To install all necessary packages run command "pip install -r requirements.txt"

## Implemented Test Tasks
1) Task 1: Data Extraction - is implemented in data_extracting.py file. 
    To run in - run command 'python data_extracting_new.py' in console.
    It will create a file pokemon.csv with required data and print items.
   
2) Task 2: Data Transformation with Apache Beam.
    To see result of this task run in the console : python data_transformation.py.
   
3) Task 3: Data Loading
    I implement loading data into the table as the step of pipeline in data_transformation.py file.
   For that I created separate file db_operations.py for better code design. And decided
   to create a DB there.
    


## Ideas to improve

Data extracting : it`s better to use JSON. But I"d faced with some  unclear
issue with readFromJson method in apache_beam package. 
There is few more ways to print the tranformed data from Task 2. I choose to print
items in the pipeline such like : using DB query(SELECT * ...) etc.
Also DB creation can be in other place. 


## About

Test tasks implemented by Konstantin. For questions or suggestion write me to email
email : konstantin.dobro@gmail.com