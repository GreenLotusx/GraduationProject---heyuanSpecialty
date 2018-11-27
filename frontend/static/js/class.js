$(function() {
	let clsid = getQueryVariable('clsid')
	getData(clsid)
})

function getData(clsid) {
	$.get('/api/query_class?clsid='+clsid, function(data) {

		if(data['error'] == 0){
			setData(data['data'])
		}
	});
}

function infosPage(cid) {
	location.href = '/infos.html?cid=' + cid;
}

function setData(data) {
	let ul = $('.commodityBox ul')
	if(data == undefined){
		let div = "<div style='min-height: 300px;font-size: 25px;line-height: 400px;text-align: center;'>没有找到相关特产记录~,请尝试一下更换关键字再重试~~</div>"
		ul.append(div)
	}else{
		$('.text').text(data['0']['class'])
		for(let i in data){
			let img = "<img src='"+data[i]['img']+"'>"
			let div1 = "<div class='price'>￥<span>" + data[i]['price'] + "</span></div>"
			let div2 = "<div class='commodityTitle'>"+data[i]['title']+"</div>"
			let div3 = "<div class='cartBox'><div class='sales fl'>销量&nbsp;&nbsp;<span>"+data[i]['sales']+"</span></div><button class='cart fl' data-id='" + data[i]['id']+ "'>加入购物车</button></div>"
			let li = "<li onclick='infosPage("+ data[i]['id'] +")';>"+img + div1 + div2 + div3 + "</li>"
			ul.append(li)
	}
	addCart();
	}
}

function addCart(cid) {
	$('.cart').click(function(event) {
		event.stopPropagation();
		let cid = $(this).data('id')
		$.get('/api/add_cart?cid='+cid + '&num=1', function(data) {
			if(data['error'] == 0){
				alert('已经成功添加到购物车')
			}else if(data['error'] == -2){
				alert('用户没有登陆')
			}else{
				alert('购物车添加失败')
			}
		});
	});
}