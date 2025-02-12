let login_try = 0;

document.getElementById("button").addEventListener("click", function() {
    const user_value = document.getElementById("user").value;
    const key_value = document.getElementById("key").value;
    const return_verify = document.getElementById("response");

    fetch('/lista_13_11/logged', {
        method: 'POST',
        body: new URLSearchParams({
            'user': user_value,
            'key': key_value
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            return_verify.textContent = data.error;
            return_verify.style.color = "red";
            login_try++;
            if (login_try >= 2) {
                return_verify.textContent = "Number of attempts exceeded. Login blocked. Try pressing F5 to try again.";
                document.getElementById("user").disabled = true;
                document.getElementById("key").disabled = true;
                document.getElementById("button").disabled = true;
            }
        } else if (data.success) {
            window.location.href = data.redirect;
        }
    })
    .catch(error => {
        return_verify.textContent = "Fail to generate the page: " + error;
        return_verify.style.color = "red";
    });
});

function clear_input() {
    document.getElementById("user").value = "";
    document.getElementById("key").value = "";
}

window.addEventListener('load', function() {
    login_try = 0;
    document.getElementById("user").disabled = false;
    document.getElementById("key").disabled = false;
    document.getElementById("button").disabled = false;
});