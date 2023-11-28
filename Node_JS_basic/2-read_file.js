const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8').split('\n').filter(Boolean);
    const headers = data[0].split(',').map((header) => header.trim());
    const studentsData = data.slice(1).map((line) => line.split(',').map((field) => field.trim()));

    const fieldIndex = headers.indexOf('field');
    const firstNameIndex = headers.indexOf('firstname');

    const studentsByField = studentsData.reduce((acc, student) => {
      const fieldName = student[fieldIndex];
      const firstName = student[firstNameIndex];

      if (fieldName && firstName) {
        if (!acc[fieldName]) {
          acc[fieldName] = { count: 0, students: [] };
        }
        acc[fieldName].count++;
        acc[fieldName].students.push(firstName);
      }
      return acc;
    }, {});

    console.log(`Number of students: ${studentsData.length}`);

    Object.keys(studentsByField).forEach((field) => {
      const { count, students } = studentsByField[field];
      console.log(`Number of students in ${field}: ${count}. List: ${students.join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
