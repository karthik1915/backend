gsap.registerPlugin(ScrollTrigger);

document.getElementById("home").addEventListener("click", function () {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});

document.getElementById("projects").addEventListener("click", function () {
  const targetPosition = window.scrollY + window.innerHeight;

  window.scrollTo({
    top: targetPosition,
    behavior: "smooth",
  });
});

document
  .getElementById("projects-title")
  .addEventListener("click", function () {
    const targetPosition = window.scrollY + window.innerHeight;

    window.scrollTo({
      top: targetPosition,
      behavior: "smooth",
    });
  });

let panels = gsap.utils.toArray(".panel");
// we'll create a ScrollTrigger for each panel just to track when each panel's top hits the top of the viewport (we only need this for snapping)
let tops = panels.map((panel) =>
  ScrollTrigger.create({ trigger: panel, start: "top top" })
);

panels.forEach((panel, i) => {
  ScrollTrigger.create({
    trigger: panel,
    start: () =>
      panel.offsetHeight < window.innerHeight ? "top top" : "bottom bottom", // if it's shorter than the viewport, we prefer to pin it at the top
    pin: true,
    pinSpacing: false,
  });
});

let navContainer = document.getElementById("navContainer");

ScrollTrigger.create({
  trigger: ".projects",
  start: "top-=25 top",
  end: "bottom top",
  onEnter: () => {
    navContainer.classList.remove("nav-container");
    navContainer.classList.add("nav-container-dark");
  },
  onLeaveBack: () => {
    navContainer.classList.remove("nav-container-dark");
    navContainer.classList.add("nav-container");
  },
});
function toggleMenu() {
  var menu = document.getElementById("popup-menu");
  let popupAnimation = gsap.fromTo(
    menu,
    {
      scale: 0,
    },
    {
      scale: 1,
      ease: "bounce.out",
      duration: 0.3,
      display: "block",
    }
  );
  popupAnimation.play();
}

document.addEventListener("click", function (event) {
  var menu = document.getElementById("popup-menu");
  var target = event.target;
  var menuBtn = document.querySelector(".menu");

  if (!menu.contains(target) && target !== menuBtn) {
    let popupAnimation = gsap.fromTo(
      menu,
      {
        scale: 1,
      },
      {
        scale: 0,
        duration: 0.3,
        display: "none",
      }
    );
    popupAnimation.play();
  }
});
