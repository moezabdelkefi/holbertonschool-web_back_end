const express = require('express');
const fs = require('fs').promises;

const app = express();

const getData = async (database) => {
  try {
    const data = await fs.readFile(database, 'utf8');
    const students = data.split('\n').filter((line) => line);

    if (students.length) {
      students.shift();
    }

    const csStudents = students.filter((line) => line.includes('CS'));
    const sweStudents = students.filter((line) => line.includes('SWE'));
    return {
      students,
      csStudents,
      sweStudents,
    };
  } catch (error) {
    console.error(error);
    return null;
  }
};

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const database = process.argv[2];
  if (!database) {
    res.status(500).send('Database not provided');
    return;
  }

  const data = await getData(database);
  if (data) {
    res.send(
      `This is the list of our students\nNumber of students: ${data.students.length}\n`
      + `Number of students in CS: ${data.csStudents.length}. List: ${data.csStudents.join(', ')}\n`
      + `Number of students in SWE: ${data.sweStudents.length}. List: ${data.sweStudents.join(', ')}`,
    );
  } else {
    res.status(500).send('Cannot read the database');
  }
});

const port = 1245;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

module.exports = app;
