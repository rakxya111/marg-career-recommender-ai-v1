document.getElementById('signup-form').addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Account created successfully!');
});

const password = document.getElementById("password");
const eyeIconPassword = document.getElementById("eyeIconPassword");

const confirmPassword = document.getElementById("confirmPassword");
const eyeIconConfirmPassword = document.getElementById("eyeIconConfirmPassword");

eyeIconPassword.onclick = function () {
  if (password.type === "password") {
    password.type = "text";
    eyeIconPassword.className = "fas fa-eye-slash toggle-eye";
  } else {
    password.type = "password";
    eyeIconPassword.className = "fas fa-eye toggle-eye";
  }
};

eyeIconConfirmPassword.onclick = function () {
  if (confirmPassword.type === "password") {
    confirmPassword.type = "text";
    eyeIconConfirmPassword.className = "fas fa-eye-slash toggle-eye";
  } else {
    confirmPassword.type = "password";
    eyeIconConfirmPassword.className = "fas fa-eye toggle-eye";
  }
};