const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        if (lines.length <= 1) {
          reject(new Error('Cannot load the database'));
        } else {
          const students = lines.slice(1);
          const studentsData = {};

          students.forEach((student) => {
            const [firstName, lastName, age, field] = student.split(',');
            if (!studentsData[field]) {
              studentsData[field] = [];
            }
            studentsData[field].push(firstName);
          });

          const totalStudents = students.length;
          console.log(`Number of students: ${totalStudents}`);

          for (const field in studentsData) {
            if (Object.prototype.hasOwnProperty.call(studentsData, field)) {
              const studentsInField = studentsData[field].length;
              console.log(`Number of students in ${field}: ${studentsInField}. List: ${studentsData[field].join(', ')}`);
            }
          }
          resolve();
        }
      }
    });
  });
}

module.exports = countStudents;
