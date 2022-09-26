const judul = document.getElementById("judul");
judul.style.color = "red";
judul.style.backgroundColor = "#ccc";
judul.innerHTML = "kelvin kleden";

const p = document.querySelectorAll("p");

for (let i = 0; i < p.length; i++) {
  p[i].style.backgroundColor = "lightblue";
}

const li2 = document.querySelectorAll("section#b ul li");
for (let i = 0; i < li2.length; i++) {
  li2[i].style.backgroundColor = "orange";
}
