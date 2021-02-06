window.onload = function(){
  $('.lecture-card').on('click', function(){
    target = $(this).attr("name")
    console.log(target)
	  window.location.href = "lecture_info/"+target
  });
};