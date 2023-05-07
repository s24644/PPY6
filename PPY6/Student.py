class Student:
    def __init__(self, email, first_name, last_name, grades, final_grade, status):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
        self.final_grade = final_grade
        self.status = status

    def assign_final_grade(self, points):
        if (points <= 50):
            return 2
        elif (points <= 60):
            return 3
        elif (points <= 70):
            return 3.5
        elif (points <= 80):
            return 4
        elif (points <= 90):
            return 4.5
        else:
            return 5

    def assign_grade(self):
        total_points = 0
        homework_percents = 0
        for i in range (4, 14):
            homework_percents += self.grades[i]

        tmp_grades = list()
        tmp_grades.append(self.grades[1])
        tmp_grades.append(self.grades[2])
        tmp_grades.append(self.grades[3])
        tmp_grades.sort()

        if homework_percents/10 >= 80:
            tmp_grades[0] = 20
            tmp_grades[1] = 20
            tmp_grades[2] = 20
        elif homework_percents/10 >= 70:
            tmp_grades[0] = 20
            tmp_grades[1] = 20
        elif homework_percents/10 >= 60:
            tmp_grades[0] = 20

        self.grades[1] = tmp_grades[0]
        self.grades[2] = tmp_grades[1]
        self.grades[3] = tmp_grades[2]

        for i in range(0, 4):
            total_points += self.grades[i]

        print("total points", total_points)

        if min(self.grades) >= 0:
            self.final_grade = self.assign_final_grade(total_points)
            print("final grade: ", self.final_grade)
        else:
            print("braki w ocenach - końcowa nie została wystawiona")

    def print_grades(self, grades):
        result_string = ""
        for i in grades:
            result_string += str(i) + ","
        return result_string[0:len(result_string)-2]

    def __str__(self):
        return self.email+","+self.first_name+","+self.last_name+","+self.print_grades(self.grades)+ ","+str(self.final_grade)+ ","+self.status



