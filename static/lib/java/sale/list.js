window.onload=function(){
//declaracion de variables y constantes
	
const btnOrder= document.getElementById('btnOrderList');
const tipo= document.getElementById('btnOpcion');

//crear nueva orden
btnOrder.addEventListener('click',(e)=>{
	let opcion=btnOpcion.value
	createOrder(opcion)
})
    const createOrder = (opcion)=>{
        let url = "/sale/inicia"
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
		body:JSON.stringify([opcion])
        })
            .then((response)=>{
                return response.json();
            })
            .then((data)=>{
                console.log('data:',data)
            })
}
}
