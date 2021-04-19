function showDetails(){
    let v = document.querySelector('.button');
    v.addEventListener('click', function(){
        let x = document.querySelector('.pinfo')
        if (x.style.display === "none") {
            x.style.display = "block";
          } else {
            x.style.display = "none";
          }
    })
}

window.onload=showDetails();