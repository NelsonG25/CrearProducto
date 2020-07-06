function confirmarEliminacion(id) {
  Swal.fire({
    title: '¿Estas seguro de eliminar?',
    text: "No podrás deshacer esta acción",
    type: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.value) {
      window.location.href = "/eliminar_proveedor/"+id+"/";
    }
  })
}
