document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");
  const messageDiv = document.getElementById("formMessage");

  // Check that elements exist
  if (!form || !messageDiv) {
    console.error("Form or message div not found");
    return;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Stop page reload

    // Show success message
    messageDiv.innerText = "Thank you! Your message has been sent.";
    messageDiv.style.color = "#0a1a3f";
    messageDiv.style.display = "block";

    // Clear the form
    form.reset();

    setTimeout(() => {
      messageDiv.style.display = "none";
    }, 5000);
  });
});
