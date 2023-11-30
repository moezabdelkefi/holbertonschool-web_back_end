/* eslint-disable no-unused-vars */
// utils.js
import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        const lines = data.trim().split('\n').slice(1);
        const students = {};
        lines.forEach((line) => {
          const [firstname, lastname, age, field] = line.split(',');
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(firstname);
        });
        resolve(students);
      }
    });
  });
}

export default readDatabase;
