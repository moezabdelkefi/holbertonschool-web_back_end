// StudentsController.js
import { readDatabase } from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase('./database.csv');
      if (!students) {
        throw new Error('Cannot load the database');
      }

      const fields = Object.keys(students).sort((a, b) => a.localeCompare(b));
      let response = 'This is the list of our students\n';
      fields.forEach((field) => {
        response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const { major } = req.params;
      if (major !== 'CS' && major !== 'SWE') {
        throw new Error('Major parameter must be CS or SWE');
      }

      const students = await readDatabase('./database.csv');
      if (!students) {
        throw new Error('Cannot load the database');
      }

      if (!students[major]) {
        res.status(200).send(`No students found in ${major}`);
      } else {
        const response = `List: ${students[major].join(', ')}`;
        res.status(200).send(response);
      }
    } catch (error) {
      res.status(500).send(error.message);
    }
  }
}

export default StudentsController;
