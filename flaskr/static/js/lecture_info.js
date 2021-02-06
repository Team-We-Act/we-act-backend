window.onload = function(){
  $('#question').on('click', function(){
    console.log('clicked logged')
    $("#answer").css("visibility", "visible");

  });
}