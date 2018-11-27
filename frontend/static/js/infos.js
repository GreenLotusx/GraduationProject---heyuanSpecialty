$(function() {
	let cid = getQueryVariable('cid');
	getCommodityData(cid);
	addCartBtn(cid);
	nowBuy(cid);
	numChange();
})

function getCommodityData(cid) {
	$.get('/api/commodity_data?cid='+cid, function(data) {
		if (data['error'] == 0){
			setData(data['data'])
		}
	});
}

function addCartBtn(cid) {
	$('.cart').click(function(event) {
		let num = $('.number .num_show').val()
		addCart(cid,num)
	});
}


function addCart(cid,num) {
	$.get('/api/add_cart?cid='+cid + '&num='+num, function(data) {
		if(data['error'] == 0){
			alert('已经成功添加到购物车')
		}else{
			alert('购物车添加失败')
		}
	});
}

function setData(data) {
	$('#classPage').text(data['class'][1])
	$('#classPage').attr('href','class.html?clsid='+ data['class'][0]);
	$('.picture').attr('src',data['img']);
	$('.words').text(data['infos']);
	$('.commodityTitle').text(data['title']);
	$('.customary S').text('￥'+data['ordprice']);
	$('.current h1').text('￥'+data['newprice']);
	$('.current').append('/' + data['specifications'])
	$('#server').text('￥'+data['freight']);
	$('.salesVolume span').text(data['sales']);
}

function nowBuy(cid) {
	$('.now').click(function(event) {
		let value = "cid1="+ cid +"&num1="+ $('.num_show').val() +"&num=1"+"&from=buy"
		location.href = '/place_order.html?' + value;
	});
}


function numChange() {
	let li = $('.number')
	let num
	let num_show
	console.log(li.find('.add'))
	li.find('.add').click(function(event) {
		console.log('加')
		num_show = li.find('.num_show')
		num = num_show.val()
		num++;
		num_show.val(num)
	});

	li.find('.minus').click(function(event) {
		console.log('减')
		num_show = li.find('.num_show')
		num = num_show.val()
		if (num == 1){
			num = 1;
		}else{
			num--;
		}
		num_show.val(num)
	});

}