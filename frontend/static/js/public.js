$(function(argument) {
	check_login();
	search();
})

function check_login(){
	$.ajax({
		url: '/api/check_login',
		type: 'GET',
		dataType: 'json',
	})
	.done(function(data) {
		// console.log(data)
		let html
		if (data['error'] == 0){
			html = template('alreadyLogin',data['data'])
		}else if(data['error'] == -2){
			html = template('notLogin')
		}
		$('.headerBox').html(html);
	})
	.fail(function() {
		alert('服务器异常')
	})
}

function logout() {
	$.get('/api/logout', function(data) {
		if (data['error'] == 0){
			location.href = '/index.html';
		}else if(data['error'] == -5){
			alert('注销失败,请刷新重试')
		}
	});
}

//获取url传入参数
function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}

function getCookie(name){
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function search() {
	$('#search').click(function(event) {
		event.preventDefault();
		let originalData = $(".searchBody form").serializeArray();
		location.href = '/search.html?keyword='+originalData[0]['value'];
	});
}