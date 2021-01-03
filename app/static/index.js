function addPin() {
    var url, response; 

    url = "http://127.0.0.1:5000/token"
    response = fetch(url, {method: "GET"}); 

    response.then(res => {
        res.json().then(data => {
            let pin = data["body"]["pin"]
            let element = document.getElementById("encrypted"); 
            element.value = pin; 
        })
    })
}


addPin();
setInterval(addPin, 60 * 1000);
