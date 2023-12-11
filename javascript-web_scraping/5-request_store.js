#!/usr/bin/node

import request from 'request';
import { writeFile, readFileFileSync } from 'fs';

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`${readFileFileSync(filePath, 'utf-8')}`);
      }
    });
  }
});
