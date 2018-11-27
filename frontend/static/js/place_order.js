$(function() {
	let cid = getStaticData();
	getData(cid);
	setAddress();
	$('#order_btn').click(function(event) {
		order();
	});
})


function getStaticData(argument) {
	sumNum = getQueryVariable('num')
	let cidList = new Array();
	for (var i = 1; i <= sumNum; i++) {
		console.log('循环'+i)
		cid = getQueryVariable('cid'+i)
		cnum = getQueryVariable('num'+i)
		let itemList = new Array();
		itemList.push(cid,cnum)
		cidList.push(itemList)
	}
	return cidList
}

function getData(cidList) {
	$.ajax({
		url: '/api/query_many',
		type: 'POST',
		dataType: 'json',
		contentType:'application/json',
		headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
		data: JSON.stringify({cidList:cidList}),
	})
	.done(function(data) {
		if(data['error'] == 0){
			setData(data['data'])
			setMoney();
		}
	})
	.fail(function() {
		alert('服务器异常')
	})
	
}

function setData(data) {
	let html = template('ordList', {"ordList" : data})
	$('.goods_list_th').append(html);
}

function setAddress(argument) {
	$.get('/api/user_infos', function(data) {
		if(data['error'] == 0){
			$('#address').append(data['data']['ui_address'])
		}else{
			$('#address').append('请求用户收获地址出错')
		}
	});
}

function setMoney(argument) {
	let money = 0
	let freight = 0
	let sum = 0
	let cSum = 0

	$('.goods_list_td').each(function(index, el) {
		cSum ++;
		freight += parseInt($(this).find('.col04').text())
		money += parseInt($(this).find('.col07').text())
	});

	sum = money + freight
	$('.total_goods_count em').text(cSum)
	$('.total_goods_count b').text(money.toFixed(2)+ '元')
	$('.transit b').text(freight.toFixed(2)+ '元')
	$('.total_pay b').text(sum.toFixed(2) + '元')

}


function order() {
	let cidList = getStaticData();
	$.ajax({
		url: '/api/order',
		type: 'POST',
		dataType: 'json',
		contentType:'application/json',
		headers:{"X-XSRFTOKEN":getCookie("_xsrf")},
		data: JSON.stringify({cidList:cidList,orderFrom:getQueryVariable('from')}),
	})
	.done(function(data) {
		if(data['error'] == 0){
			let ispay = pay();
			if(ispay == true){
				goPay(data['data']['orderNum']);
			}else{
				show('订单已经成功提交~')
			}
		}else{
			alert('订单提交失败！')
		}
	})
	.fail(function() {
		alert('服务器异常')
	})
}

function pay() {
// 弹出确认模拟付款的窗口
 var msg = "订单已经成功提交,需要进行模拟付款操作吗？"; 
 if (confirm(msg)==true){ 
  return true; 
 }else{ 
  return false; 
 }
}


 function goPay(oid) {
 	$.get('/api/pay?orderNum='+oid, function(data) {
 		if(data['error'] == 0){
 			show('订单付款成功!');
 		}else{
 			show('模拟付款出错！')
 		}
 	});
 }

 function show(text) {
	// localStorage.setItem('order_finish',2);
	$('.popup p').text(text)
	$('.popup_con').fadeIn('fast', function() {
		setTimeout(function(){
			$('.popup_con').fadeOut('fast',function(){
				// window.location.href = 'index.html';
			});	
		},1000)
		
	});
}