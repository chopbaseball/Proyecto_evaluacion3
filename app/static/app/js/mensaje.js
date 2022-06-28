

function eliminar(codigo){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Producto Eliminado!',
        'El producto a sido eliminado correctamente.',
        'success'
      ).then(function() {
        window.location.href="/eliminarItem/"+id
      })
    }
  })

}

function eliminar(codigo){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Producto Eliminado!',
        'El producto a sido eliminado correctamente.',
        'success'
      ).then(function() {
        window.location.href="eliminarItem/"+ codigo 
      })
    }
  })

}



function pago(){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Pagar!'
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire(
        'Pago Completado!',
        'Se a recibido la orden correctamente.',
        'success'
      )
      
    }
  })
}


function eliminarCliente (codigo){
  Swal.fire({
    title: 'Esta Seguro?',
    text: "Esta acción no se podra revertir!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Cliente Eliminado!',
          'El cliente a sido eliminado correctamente.',
          'success'
        ).then(function(){
            window.location.href ="/eliminarCliente/" + codigo;
        })
      }
  })

}

function agregar(){
  
  Swal.fire({
      title: 'Guardado!',
      text: '{{ msj }}',
      icon: 'success',
      showConfirmButton: false,
      timer: 2000
  });
                  
}

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

function  btnlateral(){
  for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var dropdownContent = this.nextElementSibling;
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        dropdownContent.style.display = "block";
      }
    });
  }
}
 