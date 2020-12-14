fetch('http://localhost:4449/api-posts/' + encodeURIComponent(id))
    .then(handleErrors)
    .then(res => res.json())
    .then(data => {
        console.log("FETCH........")
        console.log(data);
        renderPost(data);
        console.log(data);} )
    .catch(error => console.log(error) );

const url55 = 'http://localhost:5000/posts/';
const url = 'http://localhost:4449/posts/';

function handleErrors(response) {
    if (!response.ok) {
        handleError(response);
        throw Error(response.statusText);
    }
    return response;
}

function handleError(response){
    let h3 = document.createElement('h3');
    h3.innerHTML = response.status + " " + response.statusText
    document.getElementById("container-post").appendChild(h3);
}

function renderPost(data){
    console.log(typeof(session_logged))
    console.log(data);
    console.log(session_name);
    console.log(session_id);

    let h3 = document.createElement('h3');
    let p1 = document.createElement('p');
    let p2 = document.createElement('p');
    let p3 = document.createElement('p');
    let pre = document.createElement('pre');
    let img = document.createElement('img');
 
	const newDiv = document.createElement("div"); 
    newDiv.className = 'row posts'

    const newDiv2 = document.createElement("div"); 
    newDiv2.className = 'col-lg-8 col-md-10 mx-auto';
    newDiv2.id = 'view-post';

    newDiv.appendChild(newDiv2);

    h3.innerHTML = data['title'];
    newDiv2.append(h3);
    
    p1.innerHTML = 'By ' + data['name']
    newDiv2.append(p1);

    p2.innerHTML = 'Created at ' + data['created_at']
    newDiv2.append(p2);

    pre.innerHTML = data['contents'];
    p3.append(pre);
    newDiv2.append(p3);


    const cur = document.getElementById('container-post');
    cur.appendChild(newDiv);

    const imgDiv = document.createElement("div"); 
    imgDiv.className = 'col-lg-4 col-md-2 mx-auto';
    newDiv.appendChild(imgDiv);

    img.src = data['img'];
    img.id = 'post-image';
    imgDiv.appendChild(img);
    
    if(session_logged == true){
       if (data['owner'] == session_id || session_name == 'admin'){
              
            var a = document.createElement('a');  
            var link = document.createTextNode("Edit your post"); 
            a.appendChild(link);  
            a.title = "This is Link";  
            a.href = url + data['post_id'] + '/edit';  
            a.className = 'btn btn-primary';

            newDiv2.append(a);

            var a_delete = document.createElement('a');  
            var link2 = document.createTextNode("Delete your post"); 
            a_delete.appendChild(link2);  
            a_delete.title = "This is Link";  
            a_delete.href = url + data['post_id'] + '/delete';  
            a_delete.className = 'btn btn-danger';

            newDiv2.append(a_delete);
       }  
    }
}
