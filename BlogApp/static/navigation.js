    const token = window.localStorage.getItem('token');
   
    function decode_token(token){
        try {
            return JSON.parse(atob(token.split('.')[1]));
          } catch (e) {
            return null;
          }
    }
    var decoded_token = decode_token(token);
    var current_user;
    var user_id;
    document.addEventListener('DOMContentLoaded', (event) => {
        if ( typeof(decoded_token) !== "undefined" && decoded_token !== null ) {
            current_user = decoded_token['sub']['name'];
            user_id = decoded_token['sub']['user_id'];
            if(current_user !== 'admin'){
                 const element1 = document.getElementById('users-btn');
                 element1.classList.add('hide');
            }
            const element = document.getElementById('login-btn');
            element.classList.add('hide');
        }else{
             const element = document.getElementById('logout-btn');
             element.classList.add('hide');

             const element1 = document.getElementById('users-btn');
             element1.classList.add('hide');
        }
    })

    function edit(){
        let a = document.getElementById('edit-btn');
        a.href = '/users/edit' + user_id + '/edit';
    }

    function logout(){
        event.preventDefault();
       
        console.log("logout");
        fetch('/api-posts/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            }
        }).then(response => {
            console.log(response);
            if(response.ok){
                window.localStorage.removeItem('token');
                window.location.replace("/");
            }
            return response.json()
        }).then(data =>
            console.log(data))
        .catch(error => console.log(error));
    }
