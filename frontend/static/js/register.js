$(function(){
	window.error_name = false;
	window.error_password = false;
	window.error_check_password = false;
	window.error_email = false;
	window.error_check = false;
	cheack();
	submit();
})

function cheack() {
	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			window.error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			window.error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});
}


function check_user_name(){
	var len = $('#user_name').val().length;
	if(len<5||len>20)
	{
		$('#user_name').next().html('请输入5-20个字符的用户名')
		$('#user_name').next().show();
		window.error_name = true;
	}
	else
	{
		$('#user_name').next().hide();
		window.error_name = false;
	}
}

function check_pwd(){
	var len = $('#pwd').val().length;
	if(len<8||len>20)
	{
		$('#pwd').next().html('密码最少8位，最长20位')
		$('#pwd').next().show();
		window.error_password = true;
	}
	else
	{
		$('#pwd').next().hide();
		window.error_password = false;
	}		
}

function check_cpwd(){
	var pass = $('#pwd').val();
	var cpass = $('#cpwd').val();

	if(pass!=cpass)
	{
		$('#cpwd').next().html('两次输入的密码不一致')
		$('#cpwd').next().show();
		window.error_check_password = true;
	}
	else
	{
		$('#cpwd').next().hide();
		window.error_check_password = false;
	}			
}



function check_email(){
	var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

	if(re.test($('#email').val()))
	{
		$('#email').next().hide();
		window.error_email = false;
	}
	else
	{
		$('#email').next().html('你输入的邮箱格式不正确')
		$('#email').next().show();
		window.error_check_password = true;
	}
}


function submit() {
	$('#reg_form').click(function() {
		event.preventDefault();
		console.log('点击注册')
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(window.error_name == false && window.error_password == false && window.error_check_password == false && window.error_email == false && window.error_check == false)
		{
			let originalData = $(".reg_form form").serializeArray();
			let jsonData = getJsonData(originalData);
			console.log(JSON.stringify(jsonData))
			$.ajax({
				url: '/api/register',
				type: 'POST',
				dataType: 'json',
				contentType:'application/json',
				headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
				data: JSON.stringify(jsonData),
			})
			.done(function(data) {
				console.log(data);
				if(data['error'] == 0){
					alert('用户注册成功')
					location.href = '/login.html';
				}else if (data['error'] == -30){
					alert('用户已经存在')
				}else if(data['error'] == -31){
					alert('邮箱已被注册')
				}else if(data['error'] == -32){
					alert('用户注册发生错误,请刷新后重试')
				}
			})
			.fail(function() {
				console.log("error");
			})
			
		}else{
			console.log('不能提交')
		}
	})
}

function getJsonData(originalData) {
	var data = {}
	$.each(originalData,function(index, el) {
		if (el.value == ""){
			return false
		}
		data[el.name] = el.value
	});
	var newData = {}
	newData['useNumber'] = data['user_name'],
	newData['password'] = data['pwd'],
	newData['email'] = data['email']
	return newData
}

function getCookie(name){
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}