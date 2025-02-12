let login_try = 0;

document.getElementById("button").addEventListener("click", function() {
    const correct_user = "user123";
    const correct_key = "key123";

    const user_value = document.getElementById("user").value;
    const key_value = document.getElementById("key").value;
    const return_verify = document.getElementById("response");

    if (user_value === correct_user && key_value === correct_key) {
        login_try = 0;

        const time_now = new Date().getHours();
        let success_login;

        if (time_now >= 0 && time_now < 12) {
            success_login = "Good Morning!";
        } else if (time_now >= 12 && time_now < 18) {
            success_login = "Good Evening!";
        } else {
            success_login = "Good Night!";
        }

        return_verify.textContent = success_login;
        return_verify.style.color = "green";
        clear_input();

        fetch('/lista_06_11/logged', {
            method: 'POST',
            body: new URLSearchParams({
                'user': user_value,
                'key': key_value
            }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(response => response.text())
        .then(html => {
            document.open();
            document.write(html);
            document.close();
        })
        .catch(error => {
            return_verify.textContent = "Fail to generate the page: " + error;
            return_verify.style.color = "red";
        });
    } else {
        login_try++;
        if (login_try < 2) {
            return_verify.textContent = "Login has not been successful. Try one LAST time";
            return_verify.style.color = "red";
            clear_input();
        } else {
            return_verify.textContent = "Number of attempts exceeded. Login blocked / Try press F5 in 1sec for try again.";
            return_verify.style.color = "red";
            document.getElementById("user").disabled = true;
            document.getElementById("key").disabled = true;
            document.getElementById("button").disabled = true;
            clear_input();
        }
    }
});

function clear_input() {
    document.getElementById("user").value = "";
    document.getElementById("key").value = "";
}