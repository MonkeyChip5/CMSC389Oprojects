'''
Joseph Wu
CMSC389O section 0301

The problem my code solves: 
My code is able to get course information and figure out course data 
information such as how many credits the class is, who are thr professors 
who teach it, and what is the average grade of those who are taking the class.

How does my code work?
I use API calls from plannetterm.com to get course data. Then after figuring 
out the format of the returned information, I used json to extract and 
process the data I wanted.
'''

import pip._vendor.requests as requests
import json as json
import io
import csv

def num_credits(course_code):
    url = f"https://api.planetterp.com/v1/course?name={course_code}"
    response = requests.get(url)
    course_data = response.json()
    print(course_data.get('credits', 0))
    return course_data.get('credits', 0)

def get_professor(course_code):
    url = f"https://api.planetterp.com/v1/course?name={course_code}"
    response = requests.get(url) 
    professors_data = response.json()
    professors = professors_data['professors']
    print(professors)
    return professors

def avg_gpa(course_code):
    url = f"https://api.planetterp.com/v1/course?name={course_code}"
    response = requests.get(url) 
    grades_data = response.json()
    print(grades_data)
    grades = grades_data['average_gpa']
    return grades

