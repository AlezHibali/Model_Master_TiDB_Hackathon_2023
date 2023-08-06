let isStarFilled = false; // Keep track of the star's filled state

function toggleStar() {
  const starIcon = document.querySelector(".star-icon");
  isStarFilled = !isStarFilled; // Toggle the filled state
  if (isStarFilled) {
    starIcon.style.fill = "#f1c40f"; // Fill the star if it's unfilled
  } else {
    starIcon.style.fill = "transparent"; // Unfill the star if it's filled
  }
}
