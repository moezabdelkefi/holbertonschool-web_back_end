const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8').split('\n').filter(Boolean);
    const headers = data.shift().split(',').map((header) => header.trim());

    console.log(`Number of students: ${data.length}`);

    headers.forEach((field, index) => {
      const fieldStudents = data.map((line) => line.split(',')[index]).filter(Boolean);
      console.log(`Number of students in ${field}: ${fieldStudents.length}. List: ${fieldStudents.join(', ')}`);
    });
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
