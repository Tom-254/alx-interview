const request = require('request');

const movieId = process.argv[2];

const get = url => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

get(`https://swapi-api.alx-tools.com/api/films/${movieId}/`)
  .then(response => Promise.all(response.characters.map(url => get(url))))
  .then(responses => responses.map(response => response.name))
  .then(names => names.forEach(name => console.log(name)))
  .catch(error => console.error(error));