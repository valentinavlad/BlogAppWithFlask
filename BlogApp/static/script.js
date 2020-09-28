function confirm_delete() {
    if (window.confirm("Do you really want to delete this post?")) { 
          window.open("posts.html", "Thanks for Visiting!");
        }else{
        window.open("view_post.html", "Thanks for Visiting!");
    }
}