const base_url = 'http://localhost:4449/api-posts/login';
function submit_login(){
    var name = document.getElementById("name").value;
    var password = document.getElementById("password").value;
    event.preventDefault();
    console.log("You pressed login");
    let opts = {
        'username': name,
        'password': password
    };
    console.log(opts);
    value=JSON.stringify(opts)
    fetch(base_url, {
        method: 'post',
        headers: {
          "Content-Type": "application/json",
        },
        body: value
    }).then(r => {r.json();
        console.log("cucu");
        console.log(r);
        }).then((data) => {
  console.log('Success:', data);
})
        .then(token => {
        console.log(token)

        }).catch((err) => {
  return err;
});
}