class Solution:
    def countStudents(self, students, sandwiches):
        k = 0
        count = 0
        n = len(students) # do this because length of students list will keep changing as we move forward with the iterations
        while k < n-1 or count < n:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                k += 1
                count += 1
            else:
                students = self.move_student_to_end(students)
                count += 1
        if(len(students) == 0):
            return 0
        return len(students)

    def move_student_to_end(self, students):
        students = students[1:] + students[0:1]
        return students

#s = [1,2,3,4]
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(Solution().countStudents(students, sandwiches))
#Solution().move_student_to_end(s)