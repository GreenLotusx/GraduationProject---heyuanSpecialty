$(function() {
	getData();
})


function getData() {
	let keyword = getQueryVariable('keyword')
	$.get('/api/query_like?keyword='+keyword, function(data) {
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
		for(let i in data){
			let img = "<img src='"+data[i]['img']+"'>"
			let div1 = "<div class='price'>￥<span>" + data[i]['price'] + "</span></div>"
			let div2 = "<div class='commodityTitle'>"+data[i]['title']+"</div>"
			let div3 = "<div class='cartBox'><div class='sales fl'>销量<span>"+data[i]['sales']+"</span></div><button class='cart fl'>加入购物车</button></div>"
			let li = "<li onclick='infosPage("+ data[i]['id'] +")';>"+img + div1 + div2 + div3 + "</li>"
			ul.append(li)
	}
	}
}