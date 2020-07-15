function confirmarprov(event) {
  Swal.fire({
    title: 'Proveedor Agregado de manera exitosa',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'OK!'
  }).then((result) => {
    if (result.value) {
      window.location.href = "/agregar_proveedor/";
    }
  })
}
