$(function(){
  $('.btn').on('click',  function() {
    var newpwd  = $("input[name=newpwd]").val(),
      confirm_pwd = $("input[name=confirm_pwd]").val()
      if (newpwd == "" || confirm_pwd == "" || newpwd == null || confirm_pwd == null || newpwd == undefined || confirm_pwd == undefined ) {
        sweetAlert("温馨提示", '密码不允许为空',"error");  
      }
      else if(newpwd != confirm_pwd){
        sweetAlert("温馨提示", "两次输入的密码不正确","error");
      }
  })
})