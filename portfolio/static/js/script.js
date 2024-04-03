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
