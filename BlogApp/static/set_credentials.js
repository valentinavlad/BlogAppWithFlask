
function set_credentials(uid){
    
    event.preventDefault();
    console.log("uid",uid);
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var cf_password = document.getElementById("cf_password").value;

    let headers = new Headers();
    headers.set('Content-Type', 'application/json');

    
    let opts = {
        'email': email,
        'password': password,
        'cf_password': cf_password
    };

    value=JSON.stringify(opts)
    fetch('/api-posts/'+ uid +'/set_credentials', {
        method: 'post',
        headers: headers,
        body: value
    })
    .then((response) => {
        if (!response.ok) {
            handleError(response);
            throw Error(response.statusText);
        }
        return response;
    })
    .then(res => res.json())
    .then((data) => {
       window.location.replace('/auth/login');
    })
    .catch((err) => {
      console.log(err);
      return err;
    });
}


function handleError(response){
    //let h3 = document.createElement('h3');
    //h3.className = 'text-center mb-5';
    //h3.innerHTML = response.status + " " + response.statusText;
    
    //oldNode = document.getElementById("login-container")
    //oldNode.insertBefore(h3,oldNode.firstElementChild);

}