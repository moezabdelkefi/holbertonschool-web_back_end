export default function getListStudentIds(arrayofobject) {
  if (!Array.isArray(arrayofobject)) {
    return [];
  }
  return (arrayofobject.map((student) => student.id));
}
