
window.onload = function(){
  var savedVal = '';
  let volunteer_card = document.getElementById('volunteer-card');
  let recipient_card = document.getElementById('recipient-card');
  let next_button = document.getElementById('next-button');

  $('#volunteer-card').on('click', function(){
    savedVal = 'volunteer';
    if (volunteer_card.classList.contains('passive-card')) {
      $('#volunteer-card').removeClass("passive-card")
      $('#volunteer-card').addClass('volunteer-card-active');
      document.getElementById("volunteer-card__image").src = "../static/images/volunteer_active.png";
    }
    if (recipient_card.classList.contains('recipient-card-active')) {
      $('#recipient-card').removeClass("recipient-card-active")
      $('#recipient-card').addClass('passive-card');
      document.getElementById("recipient-card__image").src = "../static/images/recipient.png";
    }
    next_button.disabled = false;
  });
  
  $('#recipient-card').on('click', function(){
      savedVal = 'recipient';
      if (volunteer_card.classList.contains('volunteer-card-active')) {
        $('#volunteer-card').removeClass("volunteer-card-active");
        $('#volunteer-card').addClass('passive-card');
        document.getElementById("volunteer-card__image").src = "../static/images/volunteer.png";
      }
      if (recipient_card.classList.contains('passive-card')) {
        $('#recipient-card').removeClass("passive-card");
        $('#recipient-card').addClass('recipient-card-active');
        document.getElementById("recipient-card__image").src = "../static/images/recipient_active.png";
      }
      next_button.disabled = false;

  });

  $('#next-button').on('click', function(){
    location.href = './register_form_' + savedVal
  });
}