document.querySelector("form").addEventListener("submit",(e)=>{

const edad =
parseInt(document.querySelector('[name="edad"]').value);

if(edad < 10){

alert("Edad inválida");
e.preventDefault();

}

});