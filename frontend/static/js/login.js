$(function() {
	login();
	heidErrorMsg();
})

function getCookie(name){
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function heidErrorMsg(){
	$('#username').focus(function(event) {
		$('.user_error').addClass('invisible')
	});

	$('#password').focus(function(event) {
		$('.pwd_error').addClass('invisible')
	});
}

function login(){
	$('#input_submit').click(function(event) {
		event.preventDefault();
		userName = $('#username').val();
		passWord = $('#password').val();
	var req_data = {
		username:userName,
		password:passWord,
	}
	$.ajax({
		url: '/api/login',
		type: 'POST',
		dataType: 'json',
		contentType:'application/json',
		headers:{
			"X-XSRFTOKEN":getCookie("_xsrf"),
		},
		data: JSON.stringify(req_data),
	})
	.done(function(data) {
		if (data['error'] == 0){
			if(data['data']['identity'] > 1){					//这里判断用作管理员跳转到后台，普通用户跳转到首页
				location.href = '/index.html';
			}else if(data['data']['identity'] <= 1){
				location.href = '/backstage.html'
			}
		}else{
			$('.pwd_error').removeClass('invisible')
			$('.pwd_error').text('账号或密码错误')
		}
	})
	.fail(function() {
		alert('服务器异常！')
	})
	

	});
}
