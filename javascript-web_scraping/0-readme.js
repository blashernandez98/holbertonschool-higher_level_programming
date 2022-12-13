#!/usr/bin/node

const fs = require('fs');
const file_path = process.argv[2];

fs.readFile(file_path, 'utf-8', (err, data) => {
  if (err) throw err;

  console.log(data);
});
