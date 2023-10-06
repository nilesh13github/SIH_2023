/* When the user clicks on the button,
        toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}


document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.querySelector('form');

  loginForm.addEventListener('submit', function (e) {
      e.preventDefault(); // Prevent the default form submission

      // Get user input from the form
      const email = document.querySelector('#email').value;
      const password = document.querySelector('#password').value;

      // Perform client-side validation here (e.g., checking for empty fields)

      // Create an object to send data to the server (if needed)
      const data = {
          email: email,
          password: password
      };

      // Send an AJAX request to your server (you will need a server-side script to handle this)
      // You can use the Fetch API or XMLHttpRequest for this purpose
      // Example using Fetch API (replace with your server endpoint)
      fetch('/your-server-endpoint', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
          // Handle the server response here (e.g., show success or error messages)
          if (data.success) {
              // Redirect to a success page or perform other actions
              window.location.href = '/success-page.html';
          } else {
              // Display error message to the user
              alert(data.message);
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  });
});
