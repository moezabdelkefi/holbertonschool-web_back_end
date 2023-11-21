export default function getStudentsByLocation(studentlist, city) {
  const studentcity = studentlist.filter((student) => student.location === city);
  return studentcity;
}
