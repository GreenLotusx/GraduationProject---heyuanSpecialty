$(function() {
	changePage();
	let id = getQueryVariable('id');
	// console.log('id:'+id)
	getUserInfos();
	fileInputChange();
	submitInfos();
	submitAddress();
	submitPsd();
})


function changePage(){
	$('.body_left_bootom li').click(function(event) {
		$(this).addClass('select').siblings().removeClass('select')
		let idx = $(this).index()
		$('.body_right').each(function(index, el) {
			if (index == idx){
				let pageid = $(this).data('id')
				$(this).removeClass('invisible')
				// if (pageid == 1){

				// }else if (pageid == 2){

				// }
			}else{
				$(this).addClass('invisible')
			}
		});
	});
}

//获取用户基本信息
function getUserInfos() {
	$.get('/api/user_infos', function(data) {
		let usePic = data['data']['user_pic'];
		let sex = data['data']['user_sex'];
		let nowAddress = data['data']['ui_address'];
		let mailBox = data['data']['user_mailbox'];
		let userName = data['data']['user_name'];
		$('.pic').attr('src',usePic);
		$('.msg span').text(userName);
		$('.userName input').val(userName);
		$('.mailbox input').val(mailBox);
		$(".sex input[value="+ sex +"").attr("checked",'checked');
		$('.nowAddressBody').html(nowAddress);
		$('.body_left img').attr('src', usePic);
	});
}

//实时显示选中的图片
function fileInputChange(){
	var fr = new FileReader();
    fr.onload = function (e) {
        $('.pic')[0].src = e.target.result;
    };
	$('#picFile').change(function(event) {
	    var imgFile = this.files[0];
	    fr.readAsDataURL(imgFile);
	});
}

function getJsonData(originalData) {
	var data = {}
	$.each(originalData,function(index, el) {
		if (el.value == ""){
			alert('不能带有空值提交')
			return false
		}
		data[el.name] = el.value
	});
	return data
}


function submitInfos(argument) {
	$('#infosSave').click(function(event) {
		event.preventDefault();
		let originalData = $(".body_right_user_infos form").serializeArray();
		let formdata = new FormData();
		let fileObj = $('#picFile')[0].files[0];
		let jsonData = getJsonData(originalData);
		formdata.append('parameter',JSON.stringify(jsonData));
		formdata.append('file',fileObj)
		$.ajax({
			url: '/api/set_infos',
			type: 'POST',
			cache: false,
			processData: false,
			contentType:false,
			headers:{
			"X-XSRFTOKEN":getCookie("_xsrf")},
			data:formdata
		})
		.done(function(data) {
			if(data['error'] == 0){
				alert(data['data'])
				getUserInfos();
				check_login();
			}
		})
		.fail(function() {
			alert('服务器异常')
		})
	});
}

function submitAddress(argument) {
	$('#addressSave').click(function(event) {
		event.preventDefault();
		let originalData = $(".body_right_user_address form").serializeArray();
		let jsonData = getJsonData(originalData);
		$.ajax({
			url: '/api/set_address',
			type: 'POST',
			dataType: 'json',
			contentType:'application/json',
			headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
			data: JSON.stringify(jsonData),
		})
		.done(function(data) {
			if(data['error'] == 0){
				alert(data['data']);
				getUserInfos();
			}
		})
		.fail(function() {
			alert('服务器异常')
		})
	});
}

function submitPsd(argument) {
	$('#psdSave').click(function(event) {
		event.preventDefault();
		let originalData = $(".body_right_user_psd form").serializeArray();
		let jsonData = getJsonData(originalData);
		console.log(originalData)
		$.ajax({
			url: '/api/set_pwd',
			type: 'POST',
			dataType: 'json',
			contentType:'application/json',
			headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
			data: JSON.stringify(jsonData),
		})
		.done(function(data) {
			if(data['error'] == 0){
				alert(data['data']);
				// getUserInfos();
				logout();
				location.href = '/index.html';
			}else if (data['error'] == -20){
				alert('旧密码输入不正确')
			}else if (data['error'] == -21){
				alert('密码更新失败')
			}else if (data['error'] == -22){
				alert('新旧密码不能相同')
			}
		})
		.fail(function() {
			alert('服务器异常')
		})
	});
}