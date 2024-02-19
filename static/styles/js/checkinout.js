document.getElementById("myForm").addEventListener("submit", function(event){
    event.preventDefault();

    var username = document.getElementById("username").value;
    var badge_id = document.getElementById("badge_id").value;
    var tool_id_number = document.getElementById("tool_id_number").value;

    if(username == "" || badge_id == "" || tool_id_number == ""){
        alert("All fields must be filled out");
        return;
    }

    fetch('/checkinout', {
        method: 'POST',
        body: new FormData(document.getElementById("myForm"))
    })
    .then(response => response.json())
    .then(data => {
        if(data.status == "success"){
            alert(data.message);
        } else {
            alert("Error: " + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});