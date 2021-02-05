window.onload = function(){
  $('#login-button').on('click', function(){
    let magic_value = document.getElementById("enter-magic-code").value
    if (magic_value != 'volunteer123' && magic_value != 'recipient123') {
      console.log('no..');
    } else if (magic_value == 'volunteer123') {
      location.href = './volunteer_classes'
    } else if (magic_value == 'recipient123') {
      location.href = './recipient_classes'
    } else {
      console.log('something wrong ..');
    }
  });
  $('#enter-magic-code').on('input', function(){
    let text = document.getElementById('enter-magic-code').value;
    let login_button =  document.getElementById("login-button");
    console.log(text);
    if (text == '') {
      console.log('empty');
      if (login_button.classList.contains('active-button'))
        login_button.classList.remove("active-button");
      login_button.classList.add('passive-button');
      login_button.disabled = true;
    } else {
      if (login_button.classList.contains('passive-button'))
        login_button.classList.remove("passive-button");
      login_button.classList.add('active-button');
      login_button.disabled = false;
    }
  });
}