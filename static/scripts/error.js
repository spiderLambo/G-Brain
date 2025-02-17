const boutton = document.querySelector("button"); // Le boutton
let nbDeplacement = 0; // Le nombre de déplacement qu'a fait le boutton

// A chque fois que la souris bouge au dessu du boutton
boutton.addEventListener("mousemove", (e) => {
  // Maximum de déplacement
  if (nbDeplacement < 20) {
    // Déplacer le boutton
    boutton.style.top = `${Math.floor(Math.random() * 200)}px`;
    boutton.style.left = `${Math.floor(Math.random() * 500)}px`;
    boutton.style.right = `${Math.floor(Math.random() * 500)}px`;
    boutton.style.bottom = `${Math.floor(Math.random() * 200)}px`;
    nbDeplacement += 1; // Incrémenter le nombre de déplacement
  }
});
