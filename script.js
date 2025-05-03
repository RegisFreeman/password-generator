function generatePassword() {
  const name = document.getElementById('fullname').value.trim();
  const result = document.getElementById('result');
  const error = document.getElementById('error');

  result.style.display = "none";
  error.style.display = "none";

  if (!name) {
    error.textContent = "Please enter your full name.";
    error.style.display = "block";
    return;
  }

  const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*";
  let password = '';
  for (let i = 0; i < 12; i++) {
    const randomIndex = Math.floor(Math.random() * charset.length);
    password += charset[randomIndex];
  }

  result.textContent = "Your password: " + password;
  result.style.display = "block";
}
