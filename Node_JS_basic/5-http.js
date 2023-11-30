const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  const databasePath = process.argv[2] || './database.csv';

  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    fs.readFile(databasePath, 'utf-8', (err, data) => {
      if (err) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('Error reading database');
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      let response = 'This is the list of our students\n';

      const studentsData = {};
      students.forEach((student) => {
        // eslint-disable-next-line no-unused-vars
        const [firstName, lastName, age, field] = student.split(',');
        if (!studentsData[field]) {
          studentsData[field] = [];
        }
        studentsData[field].push(`${firstName}`);
      });

      for (const field in studentsData) {
        if (Object.prototype.hasOwnProperty.call(studentsData, field)) {
          const studentsInField = studentsData[field].length;
          response += `Number of students in ${field}: ${studentsInField}. List: ${studentsData[field].join(', ')}\n`;
        }
      }

      const totalStudents = Object.values(studentsData).flat().length;
      response += `Number of students: ${totalStudents}\n`;

      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end(response);
    });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

const port = 1245;
server.listen(port, () => {
  console.log(`Server is running and listening on port ${port}`);
});

module.exports = server;
