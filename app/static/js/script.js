$(document).ready(function(){

  if ($('.debe').text() != $('.haber').text()){
    $('.debe').addClass('bg-danger text-white');
    $('.haber').addClass('bg-danger text-white');
  }
  else{
    if($('.debe').text()=='$ 0.0' && $('.haber').text()=='$ 0.0'){
      $('.debe').addClass('bg-warning');
      $('.haber').addClass('bg-warning');
    }else{
    $('.debe').addClass('bg-success text-dark');
    $('.haber').addClass('bg-success text-dark');
    }
  }

});