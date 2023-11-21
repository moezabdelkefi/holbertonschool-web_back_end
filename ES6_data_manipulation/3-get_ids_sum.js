export default function getStudentIdsSum(studentlist) {
  const sumids = studentlist.reduce((accumulator, student) => accumulator + student.id, 0);
  return sumids;
}
