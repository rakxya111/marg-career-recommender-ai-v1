

// Function to show toast
function showToast(message, isSuccess = true) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.style.backgroundColor = isSuccess ? "#333" : "#d9534f"; // Red for error
  toast.className = "show";
  setTimeout(() => {
    toast.className = toast.className.replace("show", "");
  }, 6000); // 6 sec
}

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("contactForm");

  form.addEventListener("submit", function(e) {
    e.preventDefault(); // stop page refresh

    const formData = new FormData(form);

    fetch(form.getAttribute("action") || window.location.pathname, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCSRFToken(),
      },
      body: formData,
    })
    .then(response => {
      if (response.redirected) {
        // Django redirected, so it means success
        showToast("Successfully submitted your query. We will contact you soon.", true);
        form.reset();
      } else {
        // Likely invalid form, so reload manually to show errors
        showToast("Cannot submit your query. Please make sure all fields are valid.", false);
      }
    })
    .catch(() => {
      showToast("Something went wrong. Please try again.", false);
    });
  });
});

// CSRF helper
function getCSRFToken() {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, 10) === ('csrftoken=')) {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}
