$(function() {
	let cid = getQueryVariable('cid')
	if (cid == 0){
		submit_add();
	}else{
		getCommodityData(cid);
		submit_update(cid);
	}

	fileInputChange();
	excellentSelect();
})

//实时显示选中的图片
function fileInputChange(){
	var fr = new FileReader();
    fr.onload = function (e) {
        $('.preview img')[0].src = e.target.result;
    };
	$('#picFile').change(function(event) {
	    var imgFile = this.files[0];
	    fr.readAsDataURL(imgFile);
	});
}

function excellentSelect() {
	$('.sales input').each(function(index, el) {
		if ($(this).is(':checked')){
			$(this).val('1');
		}
	});

	$('.sales input').click(function(event) {
		if($(this).is(':checked')){
			$(this).val(1)
		}else{
			$(this).val(0)
		}
	});
}

function submit_add() {
	$('.submit').click(function(event) {
		event.preventDefault();
		let originalData = $(".main form").serializeArray();
		let jsonData = getJsonData(originalData);
		let formdata = new FormData();
		let fileObj = $('#picFile')[0].files[0];
		jsonData['hot'] = $('#hot').val()
		jsonData['excellent'] = $('#excellent').val()
		formdata.append('fromParameter',JSON.stringify(jsonData));
		formdata.append('file',fileObj);
		$.ajax({
			url: '/api/add_commodity',
			type: 'POST',
			dataType: 'json',
			cache: false,
			processData: false,
			contentType:false,
			headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
			data: formdata,
		})
		.done(function(data) {
			if (data['error'] == 0){
				alert(data['data']);
			}else{
				alert('特产添加发生异常');
			}
		})
		.fail(function() {
			alert('服务器异常')
		})
		
	});
}

function submit_update(cid) {
	console.log(cid)
		$('.submit').click(function(event) {
		event.preventDefault();
		let originalData = $(".main form").serializeArray();
		console.log(originalData)
		console.log('执行这里')
		console.log($('#hot').val())
		console.log($('#excellent').val())
		let jsonData = getJsonData(originalData);
		jsonData['hot'] = $('#hot').val()
		jsonData['excellent'] = $('#excellent').val()
		console.log('格式化后的数据')
		console.log(jsonData)
		// let cid = cid;
		let formdata = new FormData();
		let fileObj = $('#picFile')[0].files[0];
		formdata.append('cid',cid);
		formdata.append('fromParameter',JSON.stringify(jsonData));
		formdata.append('file',fileObj);
		$.ajax({
			url: '/api/update_commodity',
			type: 'POST',
			dataType: 'json',
			cache: false,
			processData: false,
			contentType:false,
			headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
			data: formdata,
		})
		.done(function(data) {
			console.log(data);
			if (data['error'] == 0){
				alert(data['data']);
			}else{
				alert('特产数据更改失败');
			}
		})
		.fail(function() {
			console.log("error");
		})
		
	});
}


function getJsonData(originalData) {
	var data = {}
	console.log(originalData)
	$.each(originalData,function(index, el) {
		if (el.value == ""){
			return false
		}
		data[el.name] = el.value
	});
	return data
}

function getCookie(name){
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
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

function getCommodityData(cid) {
	$.get('/api/commodity_data?cid='+cid, function(data) {
		console.log(data)
		if (data['error'] == 0){
			setData(data['data'])
		}
	});
	
}

function setData(data) {
	let title = data['title']
	let infos = data['infos']
	let ordprice = data['ordprice']
	let newprice = data['newprice']
	let freight = data['freight']
	let hot = data['hot']
	let excellent = data['excellent']
	let specifications = data['specifications']
	let Cclass = data['class'][0]
	let img = data['img']
	$('.title input').val(title)
	$('.infos textarea').val(infos)
	$('#ordpriceinput').val(ordprice)
	$('#newpriceinput').val(newprice)
	$('#freightinput').val(freight)
	$('#specifications').val(specifications)
	$('#pic').attr('src', img);
	$('.pic_class option').each(function(index, el) {
		if ($(this).val() == Cclass){
			$(this).attr('selected', 'select');
		}
		
	});
	if(hot == 1){
		console.log('热销为1')
		$('#hot').val('1');
		$('#hot').attr('checked', 'checked');
	}
	if (excellent == 1){
		console.log('优质为1')
		$('#excellent').val('1')
		$('#excellent').attr('checked', 'checked');
	}

}