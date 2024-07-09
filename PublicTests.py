import unittest
from solution import num_credits, get_professor, avg_gpa

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        assert num_credits("CMSC389O") == 1
    '''
def num_credits(course_code):
    url = f"https://api.planetterp.com/v1/course?name={course_code}"
    response = requests.get(url)
    course_data = response.json()
    print(course_data.get('credits', 0))
    return course_data.get('credits', 0)'''
    def test2(self):
        result = get_professor("CMSC389O")
        for prof in ['Dave Levin', 'Thomas Goldstein', 'Franklin Yang']:
          assert prof in result
    '''
def get_professor(course_code):
    url = f"https://api.planetterp.com/v1/course?name={course_code}"
    response = requests.get(url) 
    professors_data = response.json()
    professors = professors_data['professors']
    print(professors)
    return professors'''

    def test3(self):
        assert round(avg_gpa("CMSC389O"), 2) == 3.71
    '''
def avg_gpa(course_code):
    url = f"https://api.planetterp.com/v1/course?name={course_code}"
    response = requests.get(url) 
    grades_data = response.json()
    print(grades_data)
    grades = grades_data['average_gpa']
    return grades'''

if __name__ == "__main__":
    unittest.main()
