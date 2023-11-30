const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

const parseCSV = (data) => {
  const lines = data.split('\n').filter((line) => line.trim() !== '');
  const students = lines.slice(1);

  const studentsData = {};
  students.forEach((student) => {
    // eslint-disable-next-line no-unused-vars
    const [firstName, lastName, age, field] = student.split(',');
    if (!studentsData[field]) {
      studentsData[field] = [];
    }
    studentsData[field].push(`${firstName}`);
  });

  return studentsData;
};

app.get('/', (req, res) => {
  res.type('text').send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  try {
    const databasePath = './database.csv';
    const data = fs.readFileSync(databasePath, 'utf-8');

    if (data.trim() === '') {
      res.type('text').send('Empty database');
      return;
    }

    const studentsData = parseCSV(data);

    let response = 'This is the list of our students\n';
    let totalStudents = 0;

    for (const field in studentsData) {
      if (Object.prototype.hasOwnProperty.call(studentsData, field)) {
        const studentsInField = studentsData[field].length;
        response += `Number of students in ${field}: ${studentsInField}. List: ${studentsData[field].join(', ')}\n`;
        totalStudents += studentsInField;
      }
    }

    response += `Number of students: ${totalStudents}\n`;

    res.type('text').send(response);
  } catch (error) {
    res.type('text').send('Error reading database');
  }
});

app.listen(port, () => {
  console.log('...');
});

module.exports = app;
