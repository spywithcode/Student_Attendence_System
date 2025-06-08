document.addEventListener('DOMContentLoaded', () => {
    const passwordInput = document.getElementById('password');
    const togglePasswordBtn = document.querySelector('.toggle-password');
    const darkModeToggle = document.getElementById('darkModeToggle');
    const loginForm = document.getElementById('loginForm');
    const toast = document.getElementById('toast');
    const emailInput = document.getElementById('email');
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
  
    /* // Show/hide password toggle */
    togglePasswordBtn.addEventListener('click', () => {
      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        togglePasswordBtn.innerHTML = '&#128064;'; // open eye
      } else {
        passwordInput.type = 'password';
        togglePasswordBtn.innerHTML = '&#128065;'; // closed eye
      }
    });
  
    /* // Dark/light mode toggle with localStorage persistence */
    const currentMode = localStorage.getItem('darkMode');
    if (currentMode === 'enabled') {
      document.body.classList.add('dark-mode');
      darkModeToggle.textContent = '☀';
    }
  
    darkModeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
        darkModeToggle.textContent = '☀';
      } else {
        localStorage.setItem('darkMode', 'disabled');
        darkModeToggle.textContent = '🌙';
      }
    });
  
    /* // Inline validation for email and password */
    function validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    }
  
    function showValidationMessage(element, message) {
      element.textContent = message;
    }
  
    function clearValidationMessages() {
      emailError.textContent = '';
      passwordError.textContent = '';
    }
  
    /* // Toast notification */
    function showToast(message, duration = 3000) {
      toast.textContent = message;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, duration);
    }
  
  loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      clearValidationMessages();
  
      let valid = true;
      const emailValue = emailInput.value.trim();
      const passwordValue = passwordInput.value;
  
      if (!emailValue) {
        showValidationMessage(emailError, 'Email or username is required.');
        valid = false;
      } else if (!validateEmail(emailValue)) {
        showValidationMessage(emailError, 'Invalid email format.');
        valid = false;
      }
  
      if (!passwordValue) {
        showValidationMessage(passwordError, 'Password is required.');
        valid = false;
      } else if (passwordValue.length < 6) {
        showValidationMessage(passwordError, 'Password must be at least 6 characters.');
        valid = false;
      }
  
      if (valid) {
        try {
          const response = await fetch('/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: emailValue, password: passwordValue })
          });
          const data = await response.json();
          if (data.status === "success") {
            showToast(data.message);
            // Optionally disable the form or close the window here
          } else {
            showToast(data.message, 4000);
          }
        } catch (error) {
          showToast("Login failed due to an error.", 4000);
        }
      } else {
        showToast('Please fix the errors and try again.', 4000);
      }
    });
  

    // Placeholder social login button handlers
    document.querySelectorAll('.social-btn').forEach(button => {
      button.addEventListener('click', () => {
        showToast(`Social login with ${button.textContent} is not implemented.`);
     });
   });
});