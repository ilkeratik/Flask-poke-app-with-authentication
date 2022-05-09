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
        console.log(resp.responseJSON)
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
        alert(resp.responseJSON);
        window.location.href = "/dashboard";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.message).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });

  $("button.to_login_btn").click(function(e) {
    window.location.href = "/login";
  });

  //$("#search_result_wrapper")

  $("#poke_search_btn").click(function(e) {
    console.log('saass');
    var $wrapper = $("#search_result_wrapper");
    var $error_field = $("#search_result_wrapper p.error");
    $error_field.addClass("error--hidden");
    var $search_input = $("#poke_search_input");
    var $search_result_field = $("#search_result p");
    var $search_result_div = $("#search_result");
    $search_result_div.addClass("hidden")
    $.ajax({
      url: "/dashboard/pokemon/"+$search_input.val(),
      type: "GET",
      success: function(resp) {
        console.log(resp);
        $search_result_field.text(JSON.stringify(resp));
        $search_result_div.removeClass("hidden");
        return resp
      },
      error: function(resp) {
        console.log(resp.responseJSON);
        $error_field.text(resp.responseJSON.message).removeClass("error--hidden");
      }
    });
    $wrapper.removeClass("hidden");
    // if(resp.status === 200){
    //   console.log(resp.responseJSON);
    // }
  });

  $("#save_btn").click(function(e) {
    
    var $search_result_field = $("#search_result p");
    // $data = JSON.parse($search_result_field.text());
    // console.log($data)
    $.ajax({
      url: "/dashboard/save_result",
      type: "POST",
      contentType: 'application/json',
      data: $search_result_field.text(),
      dataType: "json",
      success: function(resp) {
        console.log(resp);
        console.log(resp.responseJSON);
        return resp
      },
      error: function(resp) {
        console.log(resp.responseJSON);
      }
    });

  });
  //sas123123123