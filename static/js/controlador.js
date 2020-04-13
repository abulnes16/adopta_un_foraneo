function validarCampoVacio(id) {
  if (document.getElementById(id).value == "") {
    return false;
  } else {
    return true;
  }
}

function validarSelect(id) {
  if (document.getElementById(id).value == "0") {
    return false;
  } else {
    return true;
  }
}

function verificarContras(c1, c2) {
  if (c1 == c2) {
    return true;
  } else {
    return false;
  }
}

function validarEmail(id) {
  var patron = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if (patron.test($("#" + id).val())) {
    $("#" + id).addClass("valido");
    $("#" + id).removeClass("invalido");
    $("#correo-correcto").addClass("d-block");
    $("#correo-incorrecto").removeClass("d-block");
    $("#correo-incorrecto2").removeClass("d-block");
    $("#correo-incorrecto2").addClass("d-none");
    return true;
  } else {
    $("#" + id).addClass("invalido");
    $("#" + id).removeClass("valido");
    $("#correo-incorrecto").addClass("d-block");
    $("#correo-correcto").removeClass("d-block");
    return false;
  }
}

$("#sus-landing").click(function () {
  window.location = "signup.html";
});

$("#btn-enviar-landing").click(function () {
  var v1 = validarCampoVacio("nombre-landing");
  var v2 = validarCampoVacio("correo-landing");
  var v3 = validarCampoVacio("mensaje-landing");

  if (v1 && v2 && v3) {
    var parametros =
      "usuario=" +
      $("#nombre-landing").val() +
      "&correo=" +
      $("#correo-landing").val() +
      "&mensaje=" +
      $("#mensaje-landing").val();

    console.log("Los parametros son: ", parametros);

    $("#p-vacios").addClass("d-none");
    $("#p-vacios").removeClass("d-block");
  } else {
    $("#p-vacios").removeClass("d-none");
    $("#p-vacios").addClass("d-block");
    // alert("Los campos estan vacios!!!");
  }
});

$("#btn-iniciar-sesion").click(function () {
  var nombre = validarCampoVacio("user-name");
  var contra = validarCampoVacio("user-password");

  if (nombre && contra) {
    var parametros =
      "usuario=" +
      $("#user-name").val() +
      "&contra=" +
      $("#user-password").val();

    console.log("Los parametros son: ", parametros);

    $("#p-vacios").addClass("d-none");
    $("#p-vacios").removeClass("d-block");
  } else {
    $("#p-vacios").removeClass("d-none");
    $("#p-vacios").addClass("d-block");
    // alert("Los campos estan vacios!!!");
  }
});

$("#btn-registrarse").click(function () {
  var nombre = validarCampoVacio("primer-nombre");
  var apellido = validarCampoVacio("primer-apellido");
  var genero = validarSelect("signup-gender");
  var rol = validarSelect("signup-rol");
  var correo = validarCampoVacio("signup-email");
  var telefono = validarCampoVacio("signup-phone");
  var cumple = validarCampoVacio("signup-birthday");
  var identidad = validarCampoVacio("signup-id-number");
  var nombUsuario = validarCampoVacio("signup-username");
  var contra1 = validarCampoVacio("signup-password1");
  var contra2 = validarCampoVacio("signup-password2");

  var c1 = $("#signup-password1").val();
  var c2 = $("#signup-password2").val();

  var resultContras = verificarContras(c1, c2);

  console.log("Resultados de rol y genero: ", genero, " ", rol);

  console.log("Resultado de resultContras: ", resultContras);

  if (
    nombre &&
    apellido &&
    genero &&
    rol &&
    correo &&
    telefono &&
    cumple &&
    identidad &&
    nombUsuario &&
    contra1 &&
    contra2
  ) {
    if (resultContras) {
      var parametros =
        "nombre=" +
        $("#primer-nombre").val() +
        "&apellido=" +
        $("#primer-apellido").val() +
        "&genero=" +
        document.getElementById("signup-gender").value +
        "&rol=" +
        document.getElementById("signup-rol").value +
        "&correo=" +
        $("#signup-email").val() +
        "&telefono=" +
        $("#signup-phone").val() +
        "&cumple=" +
        $("#signup-birthday").val() +
        "&identidad=" +
        $("#signup-id-number").val() +
        "&nombUsuario=" +
        $("#signup-username").val() +
        "&contra=" +
        $("#signup-password2").val();

      console.log("Los parametros son: ", parametros);

      $("#p-vacios").addClass("d-none");
      $("#p-vacios").removeClass("d-block");

      $("#contras-distintas").addClass("d-none");
      $("#contras-distintas").removeClass("d-block");
    } else {
      $("#contras-distintas").removeClass("d-none");
      $("#contras-distintas").addClass("d-block");
      // alert("Las contraseñas no concuerdan!!!");
    }
  } else {
    $("#p-vacios").removeClass("d-none");
    $("#p-vacios").addClass("d-block");
    // alert("No pueden haber campos vacios!!!");
  }
});
