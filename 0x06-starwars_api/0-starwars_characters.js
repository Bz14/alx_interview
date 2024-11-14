const id = process.argv[2];

const fetchData = async (id) => {
  const response = await fetch(`https://swapi.dev/api/films/${id}/`);
  const character = await response.json();

  for (const key of character.characters) {
    const actor = await fetchActor(key);
    console.log(actor.name);
  }
};

const fetchActor = async (url) => {
  const response = await fetch(url);
  const actor = await response.json();
  return actor;
};

fetchData(id);
