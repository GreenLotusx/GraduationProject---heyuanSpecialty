$(function(argument) {
	getData();
})


function getData() {
	$.get('/api/query_order', function(data) {
		if(data['error'] == 0){
			setData(data['data'])
		}else{
			alert('获取用户订单失败')
		}
	});
}


function setData(data) {
	if (data != undefined) {
		let html
		html = template('orderList',{"orderList":data})
		$('.right_content').html(html)
		setClick()
	}else{
		let div = "<div style='min-height: 410px;font-size: 25px;line-height: 410px;color:#616A6B;text-align: center;'>没有找到任何订单~~</div>"
		$('.right_content').html(div)
	}
}

function setClick(argument) {
	$('.oper_btn').click(function(event) {
		let id = $(this).data('id')
		if($(this).text() == '查看物流'){
			alert('本系统没有接入物流系统,无法使用此功能')
		}else if($(this).text() == '去付款'){
			let ispay = pay()
			if (ispay == true) {
				goPay(id)
			}
		}
	});
}


function pay() {
// 弹出确认模拟付款的窗口
 var msg = "确定进行模拟付款操作吗？"; 
 if (confirm(msg)==true){ 
  return true; 
 }else{ 
  return false; 
 }
}


function goPay(oid) {
 	$.get('/api/pay?orderNum='+oid, function(data) {
 		if(data['error'] == 0){
 			alert('模拟付款成功,订单已经成功支付')
 			getData();
 		}else{
 			alert('模拟付款失败！')
 		}
 	});
 }