window.alert("ANTES DE FUNCTION")
$(function () {
    window.alert("DESPUES DEL FUNCTION")
    var Toast = Swal.mixin({
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 3000
    });
    $('.swalDefaultSuccess').ready(function() {
      
      Toast.fire({
        icon: 'success',
        title: 'Usuario creado con exito'
      })
    });
  })