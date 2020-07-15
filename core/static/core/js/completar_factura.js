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