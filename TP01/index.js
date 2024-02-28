function displayYears() {
  const start = 2024;
  const end = 2028;
  const options_container = document.getElementById("year_select");
  for (let i = start; i <= end; i++) {
    const option = document.createElement("option");
    option.innerText = i;
    option.value = i;
    options_container.appendChild(option);
  }
}

function displayPHDay(dates) {
  //PH = Public Holiday -> férié
  const container = document.getElementById("PHDays_container");
  const ul = document.createElement("ul");
  container.appendChild(ul);
  dates.map((date) => {
    const li = document.createElement("li");
    li.textContent = date[0] + " :  " + date[1];
    ul.appendChild(li);
  });
}

function removePHDay() {
  const ul = document.querySelector("ul");
  if (ul != null) ul.remove();
}

async function getDataFromAPI(year) {
  const response = await fetch(
    `https://calendrier.api.gouv.fr/jours-feries/guyane/${year}.json`
  );
  const data = await response.json();
  return Object.entries(data);
}

async function main() {
  displayYears();
  let year = null;
  const select = document.getElementById("year_select");
  select.addEventListener("change", async () => {
    removePHDay();
    year = select.value;
    if (year != null) {
      const data = await getDataFromAPI(year);
      displayPHDay(data);
    }
  });
}

main();
