
const base_url = 'http://localhost:4449/api-posts/login';
function submit_login(){
    event.preventDefault();
    var username = document.getElementById("name").value;
    var password = document.getElementById("password").value;

    let headers = new Headers();
    headers.set('Authorization', 'Basic ' + btoa(username + ":" + password));
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
    .then(res => res.json())
    .then((data) => {
      console.log(data);
      set_token(data);
    })
    .catch((err) => {
      console.log(err);
      return err;
    });
}

function set_token(data){
    window.localStorage.setItem('token', data['token']);
    window.location.replace("http://localhost:4449/");
}

function handleErrors(response) {
    if (!response.ok) {
        handleError(response);
        throw Error(response.statusText);
    }
    console.log(response);
    return response;
}

function handleError(response){
    let h3 = document.createElement('h3');
    h3.className = 'text-center mb-5';
    h3.innerHTML = response.status + " " + response.statusText;
    
    oldNode = document.getElementById("login-container")
    oldNode.insertBefore(h3,oldNode.firstElementChild);

}