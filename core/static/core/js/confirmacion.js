// function agregar() {
//   Swal.fire({
//     title: 'Proveedor Añadido',
//     type: 'success',
//     timer: 3000,
//     showConfirmButton: true,
//     timerProgressBar: true,
//   },
// )};


function agregar() {
Swal.fire({
  title: 'Nuevo proveedor agregado',
  icon: 'success',
  confirmButtonText: 'OK'
}).then((result) =>{
  if (result.value) {
    Swal.fire({
    timer: 2000,
    timerProgressBar: true,
    title: 'proveedor agregado'     
    })
  }
})};


function agregarinsumo() {
  Swal.fire({
    title: 'Nuevo insumo agregado',
    icon: 'success',
    confirmButtonText: 'OK'
  }).then((result) =>{
    if (result.value) {
      Swal.fire({
      timer: 2000,
      timerProgressBar: true,
      title: 'insumo agregado'     
      })
    }
  })};

function crear() {
  Swal.fire({
    title: 'Nuevo producto creado',
    icon: 'success',
    confirmButtonText: 'OK'
  }).then((result) =>{
    if (result.value) {
      Swal.fire({
      timer: 2000,
      timerProgressBar: true,
      title: 'producto agregado'     
      })
    }
  })};

  
function facAgreg() {
  Swal.fire({
    title: 'Nueva factura enviada',
    icon: 'success',
    confirmButtonText: 'OK'
  }).then((result) =>{
    if (result.value) {
      Swal.fire({
      timer: 2000,
      timerProgressBar: true,
      title: 'producto agregado'     
      })
    }
  })};

function ordAgreg() {
  Swal.fire({
    title: 'Nueva factura enviada',
    icon: 'success',
    confirmButtonText: 'OK'
  }).then((result) =>{
    if (result.value) {
      Swal.fire({
      timer: 2000,
      timerProgressBar: true,
      title: 'producto agregado'     
      })
    }
  })};



function addPerson(e) {
  e.preventDefault();
  const row = createRow({
    name: $('#name').val(),
    lastname: $('#lastname').val()
  });
  $('table tbody').append(row);
  clean();
}

function createRow(data) {
  return (
    `<tr>` +
      `<td>${$('tbody tr').length + 1}</td>` +
      `<td>${data.name}</td>` +
      `<td>${data.lastname}</td>` +
    `</tr>`
  );
}

function clean() {
  $('#name').val('');
  $('#lastname').val('');
  $('#name').focus();
}
