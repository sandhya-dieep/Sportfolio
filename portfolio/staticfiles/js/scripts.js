document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");
  const message = document.getElementById("formMessage");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      message.innerText = "✅ Thank you! Your message has been sent.";
      message.style.color = "lightgreen";

      // clear inputs
      form.reset();
    });
  }
});

