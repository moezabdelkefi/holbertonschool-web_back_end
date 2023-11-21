function updateStudentGradeByCity(studentList, city, newGrades) {
  const updatedStudents = studentList
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeInfo = newGrades.find((grade) => grade.studentId === student.id);

      if (gradeInfo) {
        return { ...student, grade: gradeInfo.grade };
      }
      return { ...student, grade: 'N/A' };
    });

  return updatedStudents;
}

export default updateStudentGradeByCity;
