frameElement

function eliminar(codigo){
    Swal.fire({
        title: '¿Estas seguro de eliminar el producto?',
        text: "Esto no se puede revertir!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminalo!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Eliminado!',
            'El producto ha sido eliminado.',
            'success'
          ).then(function() {
            window.location.href = "/eliminarProducto/"+codigo+"/"
          })
        }
      })
}