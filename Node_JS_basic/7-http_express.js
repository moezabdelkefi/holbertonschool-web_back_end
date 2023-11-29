const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

const parseCSV = (data) => {
  const lines = data.split('\n').filter((line) => line.trim() !== '');
  const students = lines.slice(1);

  const studentsData = {};
  students.forEach((student) => {
    const [firstName, lastName, field] = student.split(',');
    if (!studentsData[field]) {
      studentsData[field] = [];
    }
    studentsData[field].push(`${firstName} ${lastName}`);
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

    const totalStudents = Object.values(studentsData).flat().length;
    let response = `This is the list of our students\nNumber of students: ${totalStudents}\n`;

    for (const field in studentsData) {
      if (Object.prototype.hasOwnProperty.call(studentsData, field)) {
        const studentsInField = studentsData[field].length;
        response += `Number of students in ${field}: ${studentsInField}. List: ${studentsData[field].join(', ')}\n`;
      }
    }

    res.type('text').send(response);
  } catch (error) {
    res.type('text').send('Error reading database');
  }
});

app.listen(port, () => {
  console.log(`Server is running and listening on port ${port}`);
});

module.exports = app;
