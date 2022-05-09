$("form[name=login_form]").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
      url: "/user/login",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        console.log(resp.data)
        window.location.href = "/dashboard";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.message).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });

  $("form[name=register_form]").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/register",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        console.log(resp.responseJSON)
        window.location.href = "/dashboard";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.message).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });

  $("a.login_link").click(function(e) {
    window.location.href = "/login";

  });

  //sas123123123