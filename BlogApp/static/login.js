
const base_url = '/api-posts/login';
function submit_login(){
    event.preventDefault();
    var username = document.getElementById("name").value;
    var password = document.getElementById("password").value;
    console.log(username);
    let headers = new Headers();
    headers.set('Content-Type', 'application/json');

    
    let opts = {
        'username': username,
        'password': password
    };

    value=JSON.stringify(opts)
    fetch(base_url, {
        method: 'post',
        headers: headers,
        body: value
    })
    .then(handleErrors)
        .then(res =>  res.json())
    .then((data) => {

        if (data.user_id) {
            return window.location.replace('/users/' + data.user_id + '/set_credentials');
        }
        window.localStorage.setItem('token', data['auth_token']);
        redirect_home();
    })
    .catch((err) => {
      console.log(err);
      return err;
    });
}

function redirect_home(){
    window.location.replace("/");
}

function handleErrors(response) {
    if (!response.ok) {
        handleError(response);
        throw Error(response.statusText);
    }
    return response;
}

function handleError(response){
    let h3 = document.createElement('h3');
    h3.className = 'text-center mb-5';
    h3.innerHTML = response.status + " " + response.statusText;
    
    oldNode = document.getElementById("login-container")
    oldNode.insertBefore(h3,oldNode.firstElementChild);

}